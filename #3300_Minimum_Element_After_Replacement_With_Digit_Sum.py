#First approach (String conversion, slower)

class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        
        for i in range(n):

            s = str(nums[i])
            elem_sum = 0

            for char in s:
                elem_sum += int(char)

            nums[i] = elem_sum
                
        return min(nums)        


#Second Approach (Simple number approach) 

class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
          
            x=nums[i]
            rev=0
          
            while x>0:
              
                rem=x%10
                rev+=rem
                x//=10
              
            nums[i]=rev
          
        return min(nums)
