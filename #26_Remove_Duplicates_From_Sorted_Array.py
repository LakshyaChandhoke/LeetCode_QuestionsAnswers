class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: an empty list has 0 unique elements
        if not nums:
            return 0

        # Slow pointer 'i': tracks the position of the last confirmed unique element
        i = 0

        # Fast pointer 'j': scans through the remaining elements
        for j in range(1, len(nums)):
            # When a new, non-duplicate element is found:
            if nums[j] != nums[i]:
                i += 1              # Advance the slow pointer to the next write slot
                nums[i] = nums[j]   # Overwrite with the unique value

        # The count of unique elements 'k' is index + 1 (since i is 0-indexed)
        return i + 1
