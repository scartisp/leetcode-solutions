class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        dp = [-1] *(1+amount)
        dp[0] = 0
        if 1 == coins[0]:
            dp[1] = 1
        
        for i in range(2,len(dp)):
            for coin in coins:
                if coin > i:
                    break
                temp = i-coin
                if dp[temp] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[temp]+1
                    else:
                        dp[i] = min(dp[i], dp[temp]+1)
                

        return dp[-1]
