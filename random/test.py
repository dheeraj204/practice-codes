def plusOne(digits):
    a = ""
    l = []
    for i in digits:
        a += str(i)
    a = int(a)
    a += 1
    for i in str(a):
        l += [int(i)]
    print(l)


plusOne([1, 2, 3])
