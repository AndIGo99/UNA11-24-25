def center(cluster):
    mini = 10**100
    for x1,y1 in cluster:
        summ = 0
        for x2,y2 in cluster:
            summ += ((x2-x1)**2+(y2-y1)**2)**0.5
        if summ< mini:
            x_mini = x1
            y_mini = y1
            mini = summ
    return [x_mini,y_mini]


f = open("27_B_21425.txt")
cluster = [[],[],[]]
for s in f:
    x,y = s.replace(",",".").split()
    x,y = float(x), float(y)
    if -20 <= x <=0 and -10<= y <=10:
        cluster[0].append ([x,y])
    if 0 < x <= 25 and 10< y <=30:
        cluster[1].append ([x,y])
    if 20 <= x <= 40 and -25< y <=0:
        cluster[2].append ([x,y])


x1_c,y1_c = center(cluster[0])[0],center(cluster[0])[1]
x2_c,y2_c = center(cluster[1])[0],center(cluster[1])[1]
x3_c,y3_c = center(cluster[2])[0],center(cluster[2])[1]

mid1,mid2 = abs(int(10000*(x1_c+x2_c+x3_c)/3)),abs(int(10000*(y1_c+y2_c+y3_c)/3))
print("answer:",mid1,mid2)
