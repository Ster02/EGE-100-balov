def f(s1, s2, m): # Две кучи s1 и s2
    if s1 + s2 >= 77: # Добавляешь s2
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 * 2, m - 1)] # По очереди используешь условие сначала для s1 потом s2
    if m % 2 != 0:
        return any(h)
    else:
        return all(h) # Если после неудачного хода Пети то any


print([x for x in range(1, 78) if f(7, x, 2)]) # Цифры 7 означает, что в начальный момент в первой куче было 7 камней
print([x for x in range(1, 78) if not f(7, x, 1) and f(7, x, 3)])
print([x for x in range(1, 78) if not f(7, x, 2) and f(7, x, 4)])