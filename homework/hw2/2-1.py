# 实现了给定一个正整数n，找出一个正整数列表，它们的乘积是所有和为n的正整数列表中最大的。
class Solution:
    def integerBreak(self, n: int) -> (int, list):
        # 初始化动态规划数组，每个位置存储一个 (max_product, [factors])
        # 初始条件为 dp[1] = (1, [1])
        dp = [(1, [1]) for _ in range(n + 1)]

        for i in range(2, n + 1):
            max_product = 0
            best_combination = []

            for j in range(1, int(i/2) + 1):  # 尝试所有可能的拆分方式
                # 拆分为 j 和 i-j，并比较保留和不保留 i-j 拆分后的乘积
                product_without_break = j * (i - j)
                product_with_break = j * dp[i - j][0]

                if product_without_break > max_product:
                    max_product = product_without_break
                    best_combination = [j, i - j]

                if product_with_break > max_product:
                    max_product = product_with_break
                    best_combination = [j] + dp[i - j][1]

            dp[i] = (max_product, best_combination)

        return dp[n]

sol = Solution()

n = int(input("请输入一个正整数："))

max_product, best_combination = sol.integerBreak(n)
print(f"最大乘积为：{max_product}")
print(f"最佳组合为：{best_combination}")
