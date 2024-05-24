N = int(input())
for i1 in range(1, N + 1):
    A = 0
    i = i1
    while i > 0:
        r = i % 10
        A += r**3
        i //= 10

    if A == i1:
        print(i1)
