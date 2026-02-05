class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = {}
        def dfs(i, result):
            if i >= len(coins):
                return 0
            if result == amount:
                return 1
            if result > amount:
                return 0
            if (i, result) in memo:
                return memo[(i, result)]
            memo[(i, result)] = dfs(i, result + coins[i]) + dfs(i + 1, result)
            return memo[(i, result)]
        return dfs(0, 0)
        