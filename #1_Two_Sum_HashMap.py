class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {} # This is for the seen part of a hashmap, where key = number, and value = index of that number

        for index,number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], index]

            seen[number] = index # Appending the dictionary of seen, with a new key 'number' with value 'index'
