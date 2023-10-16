# c的三次方根的牛顿迭代式，并假设c=10
def cube_root_newton(c):
    g = c
    epsilon = 0.0000000001
    while abs(g ** 3 - c) > epsilon:
        g = (2 * g + c / (g * g)) / 3
    return g

c = 10
result = cube_root_newton(c)
print(f"{c}的三次方根近似值为：{result}")