# Binary search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 2:
            return 1

        start = 1
        end = x

        import math
        while(start <= end):
            mid = start + math.floor((end - start) / 2)
            res = mid * mid
            if res == x:
                return mid
            elif res > x:
                end = mid - 1
            else: #res < x
                start = mid + 1

        return int(end)

print(Solution().mySqrt(4))