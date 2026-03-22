def rec(cur, targ):
    if cur < targ or cur == 7: # избегаемая точка семь
        return 0
    if cur == targ:
        return 1
    return rec(cur - 1, targ) + rec(cur - 3, targ) + rec(cur // 2, targ)  # Прописаны три действия

# 19 -> 10 -> 3
print(rec(19, 10) * rec(10, 3))