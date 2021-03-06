import py
from pypy.translator.translator import TranslationContext, graphof
from pypy.translator.backendopt.all import backend_optimizations
from pypy.translator.simplify import get_graph, transform_dead_op_vars
from pypy.objspace.flow.model import traverse, Block, summary
from pypy import conftest

def translate(func, argtypes, backend_optimize=True):
    t = TranslationContext()
    t.buildannotator().build_types(func, argtypes)
    t.buildrtyper().specialize()
    if backend_optimize:
        backend_optimizations(t)
    if conftest.option.view:
        t.view()
    return graphof(t, func), t

def test_remove_direct_call_without_side_effects():
    def f(x):
        return x + 123
    def g(x):
        a = f(x)
        return x * 12
    graph, _ = translate(g, [int])
    assert len(graph.startblock.operations) == 1

def test_dont_remove_external_calls():
    import os
    def f(x):
        os.close(x)
    graph, _ = translate(f, [int])
    assert len(graph.startblock.operations) > 0

def test_remove_recursive_call():
    def rec(a):
        if a <= 1:
            return 0
        else:
            return rec(a - 1) + 1
    def f(x):
        a = rec(x)
        return x + 12
    graph, _ = translate(f, [int])
    assert len(graph.startblock.operations) == 1

def test_remove_call_with_indirect_call():
    def f1(x):
        return x + 1
    def f2(x):
        return x + 2
    def g(x):
        if x == 32:
            f = f1
        else:
            f = f2
        return f(x)
    def h(x):
        a = g(x)
        return x + 42
    graph, t = translate(h, [int])
    assert len(graph.startblock.operations) == 1

def test_dont_remove_if_exception_guarded():
    def f(x):
        a = {} #do some stuff to prevent inlining
        a['123'] = 123
        a['1123'] = 1234
        return x + 1
    def g(x):
        try:
            a = f(x)
        except OverflowError:
            raise
        else:
            return 1
    graph, _ = translate(g, [int])
    assert graph.startblock.operations[-1].opname == 'direct_call'


def test_remove_pointless_keepalive():
    from pypy.rlib import objectmodel
    class C:
        y = None
        z1 = None
        z2 = None

    def g():
        return C()

    def f(i):
        c = g()
        c.y
        if i:
            n = c.z1
        else:
            n = c.z2
        objectmodel.keepalive_until_here(c, n)

    graph, t = translate(f, [bool])

    #t.view()

    for block in graph.iterblocks():
        for op in block.operations:
            assert op.opname != 'getfield'
            if op.opname == 'keepalive':
                assert op.args[0] in graph.getargs()


def test_remove_identical_variables():
    def g(code):
        pc = 0
        while pc < len(code):
            pc += 1
        return pc

    graph = TranslationContext().buildflowgraph(g)
    for block in graph.iterblocks():
        assert len(block.inputargs) <= 2   # at most 'pc' and 'code'

def test_get_graph():
    import os
    def list_basic_ops(i, j):
        l = [1,2,3]
        l.insert(0, 42)
        del l[1]
        l.append(i)
        listlen = len(l)
        l.extend(l)
        del l[listlen:]
        l += [5,6]
        l[1] = i
        return l[j]
    def external_function():
        return os.system("ls")
    graph, t = translate(list_basic_ops, [int, int], False) 
    for block in graph.iterblocks():
        for op in block.operations:
            if op.opname == "direct_call":
                print op
                graph = get_graph(op.args[0], t)
                assert graph is not None
    # an external function in RPython turns currently into
    # a call to a wrapper function which itself contains the
    # real call to a graph-less external ll function, so
    # we check recursively
    graph, t = translate(external_function, [], False) 
    found = []
    def walkgraph(graph):
        for block in graph.iterblocks():
            for op in block.operations:
                if op.opname == "direct_call":
                    print op
                    subgraph = get_graph(op.args[0], t)
                    if subgraph is None:
                        found.append(op)
                    else:
                        walkgraph(subgraph)
    walkgraph(graph)
    assert len(found) == 1

def addone(x):
    return x + 1

def test_huge_func():
    g = None
    gstring = "def g(x):\n%s%s" % ("    x = x + 1\n" * 1000, "    return x\n")
    exec gstring 
    assert g(1) == 1001
    # does not crash: previously join_blocks would barf on this
    graph, t = translate(g, [int])

def test_join_blocks_cleans_links():
    from pypy.rpython.lltypesystem import lltype
    from pypy.objspace.flow.model import Constant
    from pypy.translator.backendopt.removenoops import remove_same_as
    def f(x):
        return bool(x + 2)
    def g(x):
        if f(x):
            return 1
        else:
            return 2
    graph, t = translate(g, [int], backend_optimize=False)
    fgraph = graphof(t, f)
    fgraph.startblock.exits[0].args = [Constant(True, lltype.Bool)]
    # does not crash: previously join_blocks would barf on this
    remove_same_as(graph)
    backend_optimizations(t)

def test_transform_dead_op_vars_bug():
    from pypy.rpython.llinterp import LLInterpreter, LLException
    exc = ValueError()
    def f1():
        raise exc     # this function used to be considered side-effects-free
    def f2():
        f1()          # <- so this call was removed

    graph, t = translate(f2, [], backend_optimize=False)
    transform_dead_op_vars(graph, t)
    interp = LLInterpreter(t.rtyper)
    e = py.test.raises(LLException, 'interp.eval_graph(graph, [])')
    assert 'ValueError' in str(e.value)

class TestDetectListComprehension:
    def check(self, f1, expected):
        t = TranslationContext(list_comprehension_operations=True)
        graph = t.buildflowgraph(f1)
        if conftest.option.view:
            graph.show()
        assert summary(graph) == expected

    def test_simple(self):
        def f1(l):
            return [x*17 for x in l]
        self.check(f1, {
            'newlist': 1,
            'iter': 1,
            'next': 1,
            'mul':  1,
            'getattr': 1,
            'simple_call': 1,
            'hint': 2,
            })

    def test_with_exc(self):
        def g(x):
            return x * 17
        def free_some_stuff():
            pass
        def f1(l):
            try:
                return [g(x) for x in l]
            finally:
                free_some_stuff()
        self.check(f1, {
            'newlist': 1,
            'iter': 1,
            'next': 1,
            'getattr': 1,
            'simple_call': 4,
            'hint': 2,
            })

    def test_canraise_before_iter(self):
        def g(l):
            return l
        def f1(l):
            try:
                return [x*17 for x in g(l)]
            except ValueError:
                return []
        self.check(f1, {
            'newlist': 2,
            'iter': 1,
            'next': 1,
            'mul':  1,
            'getattr': 1,
            'simple_call': 2,
            'hint': 2,
            })

class TestLLSpecializeListComprehension:
    typesystem = 'lltype'

    def specialize(self, func, argtypes):
        from pypy.rpython.llinterp import LLInterpreter
        t = TranslationContext(list_comprehension_operations=True)
        t.buildannotator().build_types(func, argtypes)
        if conftest.option.view:
            t.view()
        t.buildrtyper(self.typesystem).specialize()
        if self.typesystem == 'lltype':
            backend_optimizations(t)
        if conftest.option.view:
            t.view()
        graph = graphof(t, func)
        interp = LLInterpreter(t.rtyper)
        return interp, graph

    def test_simple(self):
        def main(n):
            lst = [x*17 for x in range(n)]
            return lst[5]
        interp, graph = self.specialize(main, [int])
        res = interp.eval_graph(graph, [10])
        assert res == 5 * 17

    def test_mutated_after_listcomp(self):
        def main(n):
            lst = [x*17 for x in range(n)]
            lst.append(-42)
            return lst[5]
        interp, graph = self.specialize(main, [int])
        res = interp.eval_graph(graph, [10])
        assert res == 5 * 17
        res = interp.eval_graph(graph, [5])
        assert res == -42

    def test_two_loops(self):
        def main(n, m):
            lst1 = []
            lst2 = []
            for i in range(n):
                lst1.append(i)
            for i in range(m):
                lst2.append(i)
            sum = 0
            for i in lst1:
                sum += i
            for i in lst2:
                sum -= i
            return sum
        interp, graph = self.specialize(main, [int, int])
        res = interp.eval_graph(graph, [8, 3])
        assert res == 28 - 3

    def test_list_iterator(self):
        # for now, this is not optimized as a list comp
        def main(n):
            r = range(n)
            lst = [i*17 for i in iter(r)]
            return lst[5]
        interp, graph = self.specialize(main, [int])
        res = interp.eval_graph(graph, [8])
        assert res == 5 * 17

    def test_dict_iterator(self):
        # for now, this is not optimized as a list comp
        def main(n, m):
            d = {n: m, m: n}
            lst = [i*17 for i in d.iterkeys()]
            return len(lst) + lst[0] + lst[-1]
        interp, graph = self.specialize(main, [int, int])
        res = interp.eval_graph(graph, [8, 5])
        assert res == 2 + 8 * 17 + 5 * 17
        res = interp.eval_graph(graph, [4, 4])
        assert res == 1 + 4 * 17 + 4 * 17

    def test_iterate_over_constant(self):
        CONST = range(10)
        def main(n):
            lst = [x*17 for x in CONST]
            return lst[5]
        interp, graph = self.specialize(main, [int])
        res = interp.eval_graph(graph, [10])
        assert res == 5 * 17

## TODO: maxlength and fence hints are not supported by ootype
## see doc/discussion/list_comprehension_ootype.txt
##class TestOOSpecializeListComprehension(TestLLSpecializeListComprehension):
##    typesystem = 'ootype'
