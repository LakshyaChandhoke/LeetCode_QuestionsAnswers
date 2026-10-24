class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                total += nums[i - 1] ** 2
                
        return total


'''
You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

'''
