f = open("24_21421.txt").readline()

count = 0
max_c = 0
for i in  f:
    if i in "0123456789AB":
        count+=1
        if i == "0" and count == 1:
            count = 0
            s = ""
        if i in "02468A":
            max_c = max(max_c,count)
    else:
        count = 0
print(max_c)
