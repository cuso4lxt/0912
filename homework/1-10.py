# 输入字符串，去掉所有空格后输出
S = input()

S2 = ""
for char in S:
    if char != " ":
        S2 += char

print(S2)