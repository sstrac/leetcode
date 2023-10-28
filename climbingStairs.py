class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1] * n
        j = 0
        new_len = n-1
        while j < new_len:
            arr = arr[:new_len]
            arr[0] = 2
            process_possibilities(arr)
            new_len -= 1

def process_possibilities(arr):
    j = 1
    while
    if arr[j - 1] == 2:
        arr[j] = arr[j-1]
        arr[j-1] = 1



print(Solution().climbStairs(6))