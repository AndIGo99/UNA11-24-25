def step(s,i):
    if i == 0:
        if s > 87 and (s//2 <= 87):
            return 0
        else:
            return 1
    else:
        if i%2 == 0:
            if s > 87 and (s//2 <= 87): #данное условие нужно только для 21 задачи
                return 0 #данное условие нужно только для 21 задачи
            if step(s-2,i-1) == 0 or step(s//2,i-1) == 0:
                return 0
            else:
                return 1
        else:
            if step(s-2,i-1) == 0 and step(s//2,i-1) == 0:
                return 0
            else:
                return 1

for s in range(500,89,-1):
    if step(s,3) == 0: #для 19 задачи - второй параметр равен 1, для 20 - 2, для 21 -3
        print(s) 
    