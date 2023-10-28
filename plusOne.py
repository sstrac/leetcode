class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in list(str(int("".join([str(n) for n in digits])) + 1))]


print(Solution().plusOne([4,3,2,1]))