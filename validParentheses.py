class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sList = list(s)

        complete = False
        validPairs = ["[]", "{}", "()"]

        while not complete:
            startLen = len(sList)
            for v in validPairs:
                i = "".join(sList).find(v)
                if i >= 0:
                    sList.pop(i)
                    sList.pop(i) #remove both brackets, first pop shifts list over
            complete = len(sList) == startLen

        return len(sList) == 0


print(Solution().isValid("{}([])()[]"))