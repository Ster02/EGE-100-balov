from itertools import *

def u(x,y,z,w):
    return (x <= y) and z and not w

for a,b,c,d,e,f in product([0,1], repeat=6):
    t = ((0, 1, a, b),
         (1, 1, c, d),
         (1, e, 1, f))
    if len(set(t)) == len(t):
        for p in permutations('xyzw'):
            if all(u(**dict(zip(p,r))) == 1 for r in t):
                print(*p)
# y z x w