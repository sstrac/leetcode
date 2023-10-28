class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # we find the square root whole lower bound and upper bound of x
        # i.e x = 65, lb = 64 sqrt = 8, ub = 81, sqrt = 9
        # passing condition if x between these
        # while sqrt not a whole number
        # start 20% of x?
        # x = 10, 20% = 2
        # while x <= res
        # 2*2 = 4
        # 3*3 = 9
        # 4*4 = 16
        # lb = 3
        # improvement - measure factor

        i = 1
        factor = 1
        res = 1

        while res < x:
            if x / res > factor:
                factor *= 10
                i = factor
            else:
                i += 1
            res = i * i

        while res > x:
            i -= 1
            res = i * i

        return i

