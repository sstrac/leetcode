class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m

        while i < m + n:
            nums1[i] = nums2[i - m]
            i+=1

        return nums1

print(Solution().merge([1,2,5, None, None, None], 3, [4,6,7], 3))