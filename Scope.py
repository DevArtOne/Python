def myFunc():
    x = 300
    print(x)
myFunc()

def myFunct():
    w = 234
    def prnt():
        print(w)
    prnt()
myFunct()

t = 123
def fun():
    print(t)
fun()
print(t)


g = 543
def fnctn():
    g = 1234
    print(g)
fnctn()
print(g)


def glbFnc():
    global s
    s = 111
glbFnc()
print(s)

a = 222
def art():
    global a
    a = 333
art()
print(a)
