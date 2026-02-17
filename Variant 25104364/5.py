import string

def f(x, base):
    alf = '0123456789' + string.ascii_uppercase
    res = ''
    while x > 0:
        res = alf[x % base] + res
        x //= base
    return res

m = []

for i in range(1, 1000):
    N = f(i, 2)
    if i % 3 == 0:
        N = N + N[-3:]
    else:
        N = N + f((i % 3) * 3, 2)
    R = int(N, 2)
    if R < 130:
        m.append([i, R])
print(sorted(m))