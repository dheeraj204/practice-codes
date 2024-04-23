x = 1


def test():
    global x
    x = 2
    print(x)


test()
print(x)
