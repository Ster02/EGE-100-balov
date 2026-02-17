from itertools import *

pairs = 'HF FE ED DG GA AH BF BH BC CG'.split()
table = '478 38 256 15 34 37 168 127'.split()
# 45 + 35 = 34 + 11 = 44 + 1 = 45
for comb in permutations('ABCDEFGH'):
    flag = True
    for pair in pairs:
        start, end = pair
        flag &= str(comb.index(end) + 1) in table[comb.index(start)]
    if flag:
        print(comb)