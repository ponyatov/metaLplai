from metaL import *

def test_hello():
    hello = Object('hello')
    assert hello.test() ==\
        '\n<object:hello>'
    world = Object('world')
    assert world.test() ==\
        '\n<object:world>'
    hello // world
    assert hello.test() ==\
        '\n<object:hello>\n\t0: <object:world>'

def test_numbers():
    num23 = Num(23)
    num5 = Num(5.1)
    int6 = Int(6)
    mul56 = mul(num5, int6)
    add26 = add(num23, mul56)
    hexx = Hex(0xDeadBeef)
    bins = Bin(0b1101)
    add26 // hexx // bins
    assert add26.test() ==\
        '\n<op:+>' +\
        '\n\t0: <num:23.0>' +\
        '\n\t1: <op:*>' +\
        '\n\t\t0: <num:5.1>' +\
        '\n\t\t1: <int:6>' +\
        '\n\t2: <hex:0xdeadbeef>' +\
        '\n\t3: <bin:0b1101>'

def test_sexpr():
    subz = Sexpr() // Op('-') // Num(5) // Int(6)
    sexpr = Sexpr() // Op('+') // Num(23) // subz
    assert sexpr.test() ==\
        '\n<sexpr:>' +\
        '\n\t0: <op:+>' +\
        '\n\t1: <num:23.0>' +\
        '\n\t2: <sexpr:>' +\
        '\n\t\t0: <op:->' +\
        '\n\t\t1: <num:5.0>' +\
        '\n\t\t2: <int:6>'
