# First approach, using conversions between bases, and string. Also implementing zfill

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert to binary without '0b', pad to exactly 32 bits
        s = bin(n)[2:].zfill(32)
        
        # Reverse the string (read backwards)
        reversed_s = s[::-1]
        
        # Parse binary string back into an integer (base 2)
        return int(reversed_s, 2)

  # Second approach, using bitwise operators

class Solution(object):
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            # Shift res left by 1 to make room, then copy the last bit of n
            res = (res << 1) | (n & 1)
            # Shift n right by 1 to inspect the next bit
            n >>= 1
        return res
