def f(s1, s2, m):
    if s1 + s2 <= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 - 2, s2, m - 1), f(s1, s2 - 2, m - 1), f(s1 // 2 + s1 % 2, s2, m - 1), f(s1, s2 // 2 + s2 % 2, m - 1)]
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)


print([x for x in range(1, 1000) if f(23, x, 2)])
print([x for x in range(1, 1000) if not f(23, x, 1) and f(23, x, 3)])
print([x for x in range(1, 1000) if not f(23, x, 2) and f(23, x, 4)])
