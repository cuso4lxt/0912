# 如果把起始值g = c/2改为g = c或者g = c/4，对结果有影响吗
def square_root_newton(c, initial_guess):
    g = initial_guess
    epsilon = 0.0000000001  # 精度
    iteration_count = 0

    while abs(g ** 2 - c) > epsilon:
        g = (g + c/g)/2
        iteration_count += 1

    return g, iteration_count


# 测试
c_values = [2, 2000]
initial_guesses = [lambda c: c, lambda c: c / 4]

for c in c_values:
    for guess_func in initial_guesses:
        root, iterations = square_root_newton(c, guess_func(c))
        print(f"当c为{c}，初始值为{guess_func(c)}时，估计的平方根为：{root}，迭代次数：{iterations}")
