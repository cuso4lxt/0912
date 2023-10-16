# while循环笨办法求解根号2
def square_root_2():
    g = 0
    count = 0
    while abs(g**2 - 2) > 0.0001:
        g += 0.00001
        count += 1

    print(f"根号2的近似值为：{g}")
    print(f"循环次数为：{count}")  # 输出循环次数

square_root_2()