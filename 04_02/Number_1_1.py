from itertools import *

pairs = 'ЖЙ ЙД ДЕ ЕА АБ БВ ВЖ ВД ВЗ ЗБ ЗГ ГЕ'.split()
table = '79 579 689 45 248 349 12 35 1236'.split()

for comb in permutations('АБВГДЗЖЙЕ'):
    flag = True
    for pair in pairs:
        start, end = pair
        flag &= str(comb.index(end) + 1) in table[comb.index(start)]
    if flag:
        print(comb)