class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split(" ")

        length = len(a) - 1

        while a[length] == "":
            length -= 1

        return len(a[length])

print(Solution().lengthOfLastWord("   fly me   to   the moon  "))