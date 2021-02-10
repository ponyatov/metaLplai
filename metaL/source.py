from metaL import *

# generic source code block
class S(Primitive):
    def __init__(self, start=None, end=None):
        super().__init__(start)
        self.end = end
