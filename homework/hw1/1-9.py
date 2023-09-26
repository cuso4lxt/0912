# 输入一个字符串S，判断是否包含两个或两个以上连续出现的相同字符组成的字符串
# 例如，abccccda中就包含cccc这个由4个连续字符c组成的字符串

S = input()

for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        print("有连续字符")
        break
else:
    print("没有连续字符")

# for-else结构。如果for循环因为break语句结束，则else部分不会执行。如果for循环正常结束
