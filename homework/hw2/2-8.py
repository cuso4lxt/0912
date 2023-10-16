# 至少用3种方法求解pi的值，并比较他们的效率（精度保留到小数点后10位）。
import time
import random
import math

# 蒙特卡洛法
def monte_carlo(samples):
    inside_count = 0  # 记录落在圆内的点的数量
    for _ in range(samples):
        x,y = random.random(),random.random()
        if x**2 + y**2 <=1:
            inside_count += 1
    return (inside_count/samples) * 4

# 莱布尼兹级数法
def leibniz(terms):
    pi = 0.0
    for i in range(terms):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi


def nilakantha(terms):
    pi = 3.0
    for i in range(1, terms):
        term = (-1) ** (i + 1) * 4 / (2*i * (2*i + 1) * (2*i + 2))
        pi += term
    return pi


start_time = time.time()
monte_carlo_time = monte_carlo(10000000)
end_time = time.time()
print(f"Monte Carlo: {monte_carlo_time:.10f} (time taken: {end_time-start_time:.5f} seconds)")

start_time = time.time()
leibniz_time = leibniz(10000000)
end_time = time.time()
print(f"Leibniz: {leibniz_time:.10f} (time taken: {end_time-start_time:.5f} seconds)")

start_time = time.time()
nilakantha_time = nilakantha(10000000)
end_time = time.time()
print(f"Nilakantha: {nilakantha_time:.10f} (time taken: {end_time-start_time:.5f} seconds)")
