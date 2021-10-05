class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        dp = {} # # of steps : distinct ways to climb
        
        dp[0] = 0
        dp [1] = 1
        dp [2] = 2
        # dp[3] = (1+1+1)(2+1)(1+2) = 3
        # dp[4] = 5 = (1+1+1+1)(2+2)(1+2+1)(2+1+1)(1+1+2)
        for x in range(3,n+1):
            dp[x] = dp[x-2] + dp[x-1] 
            
        print(dp[n])
        return dp[n]