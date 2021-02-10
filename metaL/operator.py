from metaL import *

class Op(Active):
    pass

def add(a, b): return Op('+') // a // b
def sub(a, b): return Op('-') // a // b
def mul(a, b): return Op('*') // a // b
def div(a, b): return Op('/') // a // b
def pow(a, b): return Op('^') // a // b
