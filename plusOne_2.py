class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            return [1]
        pointer = len(digits) - 1
        while digits[pointer] == 9:
            digits[pointer] = 0
            if pointer > 0:
                pointer -= 1

        if digits[pointer] == 0 and pointer == 0:
            digits.insert(0, 1)
        else:
            digits[pointer] +=1

        return digits


print(Solution().plusOne([0]))