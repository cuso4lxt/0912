class Solution:
    def integerBreak(self, n: int) -> int:
        # 因为n不大于58，我们可以用一个列表来保存，dp[1]=1作为已知条件，值为-1表示未计算过
        dp = [1] * 2 + [-1] * (n-1) #dp[0]=1 ,dp[1] = 1, dp[2]到dp[n] = -1
        for i in range(2, n + 1):  # i从2到n
            # 依次计算出dp[i]
            for j in range(1,int(i/2)+1): # j从1到 i/2 + 1
                # 拆分为j 和 (i-j)
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j]) #因为i-j < i的，而dp[i]在之前已经计算过了
        return dp[n]

sol = Solution()

n = int(input())

result = sol.integerBreak(n)
print(result)