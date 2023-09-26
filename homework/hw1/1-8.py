# 分别用for和while循环实现对一个给定序列的倒序输出。
# 例如，给定L[1, 2, 3, 4, 5]，输出为[5, 4, 3, 2, 1]

L = [1, 2, 3, 4, 5]

length = len(L)

for i in range(length - 1, -1, -1):
    print(L[i])

i = length - 1
while i >= 0:
    print(L[i])
    i -= 1