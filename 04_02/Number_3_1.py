from itertools import *

pairs = 'FB BD DA AE EC CG GF FD GE'.split()
table = '234 136 12 157 467 25 45'.split()

for comb in permutations('ABCDEFG'):
    flag = True
    for pair in pairs:
        start, end = pair
        flag &= str(comb.index(end) + 1) in table[comb.index(start)]
    if flag:
        print(comb)