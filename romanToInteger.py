class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romans = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        a = list(s)
        i = 1
        res = 0

        while i <= len(a):
            if i == len(a):
                res += romans.get(a[i - 1])
                break
            else:
                comb = romans.get(a[i - 1] + a[i])

            if comb is not None:
                res += comb
                i += 2
            else:
                res += romans.get(a[i - 1])
                i += 1

        return res



print(Solution().romanToInt("LVIII"))