# 输入xyz三个数，将这三个数从小到大使用print函数打印出来。
x = float(input())
y = float(input())
z = float(input())

nums = [x, y, z]
nums.sort()

for num in nums:
    print(num)