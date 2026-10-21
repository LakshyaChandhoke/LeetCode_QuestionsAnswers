class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums) # The length of the nums list

        for i in range(0,n): # Choosing the first number

            for j in range(i+1, n): # Because once we ave crossed ith element, it is no longer useful to us

               if nums[i] + nums[j] == target:

                  return [i,j] # Asked for indexes
