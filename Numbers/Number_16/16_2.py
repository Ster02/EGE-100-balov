from functools import lru_cache


@lru_cache()

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2*g(n - 1) + n


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + g(n - 1) - 2*n
    else:
        return n + f(n - 1)


for i in range(1, 16):
    f(i)

print(f(14) + g(14))