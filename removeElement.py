class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        nums[:] = [num for num in nums if num != val]


nums = [3,2,2,3]
Solution().removeElement(nums, 2)
print(nums)
