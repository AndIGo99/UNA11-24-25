alf = "ДГИАШЭ"
count = 0
for l1 in "ДГШ":
    for l2 in alf:
        for l3 in alf:
            for l4 in alf:
                for l5 in "ИАЭ":
                    count+=1
print(count)