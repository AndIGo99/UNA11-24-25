import string
alf = "0123456789"+string.ascii_uppercase[:11]
for x in alf:
    summ = int("82934"+x+"2",21)+int("2924"+x+x+"7",21)+int("67564"+x+"8",21)
    if summ%20 == 0:
        print(summ/20)
        break
