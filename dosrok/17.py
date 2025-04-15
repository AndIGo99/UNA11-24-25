f = open("17_21416.txt").readlines()
maxsumm  = -1_000_000_000
count = 0

summ_otr = 0
for i in f:
    if int(i) < 0:
        summ_otr+=int(i)

for i in range(len(f)-2):
    x1 = int(f[i])
    x2 = int(f[i+1])
    x3 = int(f[i+2])
    if max(x1,x2,x3)*min(x1,x2,x3)> summ_otr:
        count+=1
        maxsumm = max(maxsumm,x1+x2+x3)
        
print(count,abs(maxsumm))
