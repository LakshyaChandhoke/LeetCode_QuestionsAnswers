# Approach 1, we convert it into binary and count the ones
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return bin(n).count('1')

  # Approach 2, check last bit and right shift

class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        while n > 0:
            counter += n & 1  # 1 if the last bit is 1, else 0
            n >>= 1           # Shift right by 1 to inspect the next bit
        return counter
