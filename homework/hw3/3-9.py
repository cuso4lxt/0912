# 算法复杂度为O（n）
def construct_array(A):
    n = len(A)

    # 初始化前缀和后缀的乘积数组
    prefix = [1] * n  # 只有n个元素1的列表
    suffix = [1] * n

    # 计算前缀乘积
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * A[i - 1]

    # 计算后缀乘积
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * A[i + 1]

    # 构造结果数组B
    B = [prefix[i] * suffix[i] for i in range(n)]

    return B

# for example
A = [1, 2, 3, 4, 5]
print(construct_array(A))  # 输出 [120, 60, 40, 30, 24]
