class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        l = len(nums)
        if target <= nums[0]:
            return 0

        max_val = nums[len(nums) - 1]
        if target == max_val:
            return l -1
        elif target > max_val:
            return l

        while i < l:
            if nums[i] < target:
                i += 1
            elif nums[i] >= target:
                return i

print(Solution().searchInsert([1,3], 3))