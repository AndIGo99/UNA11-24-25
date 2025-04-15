count = 0
for N in range(1125000,11111111111):
    for i in range(17,int(N//7)+1,10):
        if N%i == 0:
            print(N,i)
            count+=1
            break
    if count == 5:
        break