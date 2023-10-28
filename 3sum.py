class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        three_sums = []
        num_map = {}
        for n in nums:
            if num_map.get(n) is not None:
                num_map[n] += 1
            else:
                num_map[n] = 1
            if num_map.get(n) is not None and num_map.get(-n) is not None and num_map.get(0) is not None and n != 0:
                num_map[n] -= 1
                num_map[-n] -= 1
                num_map[0] -=1
                three_sums += [n, -n, 0]

        for d in num_map.key
        return three_sums


print(Solution().threeSum([2,3,4,5,6,7,-1,0,8,0,1000,-1000]))