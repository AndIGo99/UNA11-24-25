for N in range(10000):
    r = bin(N)[2:]
    if r.count("1") % 2 == 0:
        r = "10"+r[2:]+"0"
    else:
        r = "11"+r[2:]+"1"
    if int(r,2) > 480:
        print(N)
        break