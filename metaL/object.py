
###################################################### base object graph object
class Object:
    def __init__(self, V):
        # type/class tag
        self.type = self.__class__.__name__.lower()
        # scalar value
        self.value = V
        # slot{}s / attributes / associative array
        self.slot = {}
        # nest[]ed / ordered container
        self.nest = []

    ################################################################# text dump

    # `print` callback
    def __repr__(self): return self.dump()

    # use trees for tests: removed id, hashes
    def test(self): return self.dump(test=True)

    # full text tree dump
    def dump(self, cycle=[], depth=0, prefix='', test=False):
        def pad(depth): return '\n' + '\t' * depth
        # head
        ret = pad(depth) + self.head(prefix, test)
        # cycle
        if self in cycle:
            return ret + ' _/'
        # slot{}s
        for i in self.keys():
            ret += self[i].dump(cycle + [self], depth + 1, f'{i} = ', test)
        # nest[]ed
        for j, k in enumerate(self.nest):
            ret += k.dump(cycle + [self], depth + 1, f'{j}: ', test)
        # subtree
        return ret

    # short <T:V> header-only dump
    def head(self, prefix='', test=False):
        ret = f'{prefix}<{self.type}:{self.val()}>'
        if not test:
            ret += f' @{id(self):x}'
        return ret

    def val(self): return f'{self.value}'

    ################################################################# operators

    def keys(self):
        return sorted(self.slot.keys())

    # A[key]
    def __getitem__(self, key):
        assert isinstance(key, str)
        return self.slot[key]

    # A[key] = B
    def __setitem__(self, key, that):
        assert isinstance(key, str)
        assert isinstance(that, Object)
        self.slot[key] = that
        return self

    # A << B -> A[B.type] = B    <T:
    def __lshift__(self, that):
        return self.__setitem__(that.type, that)

    # A >> B -> A[B.value] = B   :V>
    def __rshift__(self, that):
        return self.__setitem__(that.value, that)

    # A // B -> A.push(B)
    def __floordiv__(self, that):
        assert isinstance(that, Object)
        self.nest += [that]
        return self

    ####################################################### subgraph evaluation

    def eval(self, env): raise NotImplementedError(self.eval, self, env)

    ############################################################# serialization

    def json(self): raise NotImplementedError(self.json, self)
