import sys
sys.setrecursionlimit(20000)
def F(n):
    if n <= 5:
        return 1
    else:
        return n+F(n-2)
print(F(2126)-F(2122))
        