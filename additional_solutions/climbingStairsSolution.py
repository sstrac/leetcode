class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        i_minus_1_ways = 2
        i_minus_2_ways = 1
        all_ways = 0

        i = 3
        while i <= n:
            all_ways = i_minus_1_ways + i_minus_2_ways
            # new setup for next iteration
            i_minus_2_ways = i_minus_1_ways
            i_minus_1_ways = all_ways
            i += 1

        return all_ways

print(Solution().climbStairs(3))