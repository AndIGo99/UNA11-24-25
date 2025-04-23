for N in range(174457,174506):
    dels = []
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            dels.append(i)
            if i != N//i:
                dels.append(N//i)
        if len(dels)>6:
            break
    if len(dels) == 6:
        print(sorted(dels))
    