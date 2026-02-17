from itertools import *

s = 'ЕИОРТЯ'
k = 1

for x in product(s, repeat=6):
    word = ''.join(x)
    if k % 2 != 0:
        if word[0] != 'Р' and word[0] != 'Т' and word[0] != 'Я':
            if word.count('И') >= 2:
                print(word, k)
    k += 1