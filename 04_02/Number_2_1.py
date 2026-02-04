from itertools import *

pairs = 'AF FE ED DC CB GA GF GE GD GC GB'.split()
table = '345 467 14 123567 147 24 245'.split()

for comb in permutations('ABCDEFG'):
    flag = True
    for pair in pairs:
        start, end = pair
        flag &= str(comb.index(end) + 1) in table[comb.index(start)]
    if flag:
        print(comb)