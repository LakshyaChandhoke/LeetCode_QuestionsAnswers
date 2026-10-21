class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Edge Cases:
        # 1. All negative numbers are not palindromes (e.g. -121 != 121-).
        # 2. Numbers ending in 0 cannot be palindromes unless the number itself is 0
        #    (because numbers cannot have leading zeros, e.g. 10 != 01).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Loop until we reach or pass the middle of the number:
        # While x is greater than reversed_half, we haven't crossed the halfway mark yet.
        while x > reversed_half:
            # Peel off the last digit
            digit = x % 10
            # Add the digit to reversed_half
            reversed_half = (reversed_half * 10) + digit
            # Remove last digit from x
            x = x // 10

        # When the loop terminates, there are two possibilities:
        # Case A (Even number of digits, e.g., 1221):
        #   x == 12, reversed_half == 12 -> x == reversed_half
        # Case B (Odd number of digits, e.g., 12321):
        #   x == 12, reversed_half == 123 -> the middle digit '3' doesn't matter,
        #   so we discard it with reversed_half // 10, leaving 12 == 12.
        return x == reversed_half or x == (reversed_half // 10)
