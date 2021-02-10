from metaL import *

# floating point (generic number)
class Num(Primitive):
    def __init__(self, V):
        Primitive.__init__(self, float(V))

# integer
class Int(Num):
    def __init__(self, V):
        Primitive.__init__(self, int(V))

# machine hexadecimal
class Hex(Int):
    def val(self): return hex(self.value)

# bit string
class Bin(Int):
    def val(self): return bin(self.value)
