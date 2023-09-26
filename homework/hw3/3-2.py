# 产生10-20间的随机浮点数

import random

# random.uniform(a, b) 是 Python 的 random 模块中的一个函数。
# 它返回一个浮点数 N，使得 a <= N < b
def generate_random_float():
    return random.uniform(10,20)

print(generate_random_float())