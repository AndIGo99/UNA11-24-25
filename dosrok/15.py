for A in range(1000):
    f = True
    for x in range(200):
        for y in range(200):
            F = (5 < y) or (x>32) or (x+2*y < A)
            if not F:
                f = False
    if f:
        print(A)
        break