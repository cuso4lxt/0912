# 在牛顿法求解根号2的程序中! 把c设为2或2000等不同值,观察运行结果。
def square_root_newton(c):
    g = c  # 初始化估计值
    epsilon = 0.0000000001  # 精度
    i = 0
    # 如果g^2与c的差的绝对值大于精度，则继续循环
    while abs(g ** 2 - c) > epsilon:
        g = (g + c/g)/2
        i = i + 1
        print(g)

    print(f"循环了{i}次")


# 测试
print("当c为2时的结果：")
square_root_newton(2)
print("\n当c为2000时的结果：")
square_root_newton(2000)
