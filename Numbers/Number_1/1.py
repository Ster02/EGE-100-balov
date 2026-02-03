from itertools import *

pairs = 'АБ БЖ ЖЕ ЕВ ВА ГА ГВ ГД ДБ ДЖ ДЕ'.split()
table = '345 367 1267 156 147 234 235 '.split()

for comb in permutations('АБВГДЕЖ'):
    flag = True
    for pair in pairs:
        start, end = pair
        flag &= str(comb.index(end) + 1) in table[comb.index(start)]
    if flag:
        print(comb)