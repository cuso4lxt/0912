# 根据蒙特卡罗法的思想，编写程序计算区间[2,3]上的定积分：（x^2 + 4xsinx)dx

import random
import math

def f(x):
    return x ** 2 + 4 * x * math.sin(x)

def monte_carlo(samples = 1000000):
    lower_bound, upper_bound = 2, 3
    max_y = 21

    points_under_curve = 0

    for _ in range(samples):
        x_rand = random.uniform(lower_bound, upper_bound)
        y_rand = random.uniform(0, 21)

        if y_rand <= f(x_rand):
            points_under_curve += 1

    ratio = points_under_curve / samples
    estimated_area = ratio * (upper_bound - lower_bound) * 21

    return estimated_area

result = monte_carlo()
print(result)