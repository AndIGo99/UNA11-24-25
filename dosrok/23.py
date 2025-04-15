def step(a,b):
    if a>b or a==35:
        return 0
    elif a==b:
        return 1
    else:
        return step(a+1,b)+step(a+2,b)+step(a*2,b)

print(step(7,13)*step(13,15)*step(15,51))