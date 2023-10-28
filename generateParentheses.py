class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # n - 1 because we should always start with 0, equivalent to (
        # 0 = (, 1 = )
        comb = [0b1] * n + [0b0] * (n-1) #000111
        pointer = len(comb) - 1
        print()





print(Solution().generateParenthesis(3))