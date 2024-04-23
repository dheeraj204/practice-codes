def romanToInt(s: str) -> int:
    ["I", V, X, L, C, D, M ]= 1, 5, 10, 50, 100, 500, 1000
    t = 0
    print(s)
    for i in s:
        print(i)
        t += i
    return t


romanToInt(s="III")
