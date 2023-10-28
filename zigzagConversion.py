class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        sList = list(s)
        res = [[] for n in range(numRows)]
        length = len(s)

        if length < numRows:
            return s

        gap = numRows - 1 if numRows > 1 else 1
        i = 0  # pointer along rows
        j = 0  # pointer along columns
        l = 0  # pointer in string

        while l < length:
            if j == 0 or j % gap == 0:
                i = 0
                while i < numRows and l < length:
                    res[i].append(sList[l])
                    l += 1
                    i += 1
                i -= 1
                j += 1
            else:
                i -= 1
                res[i].append(sList[l])
                l += 1
                j += 1

        joined = "".join(["".join(sub) for sub in res])
        return joined


print(Solution().convert("PAYPALISHIRING", 4))