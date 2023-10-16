# 辗转相除法求最大公约数

def GDB(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())

print(GDB(a,b))
