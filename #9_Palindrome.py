class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers can never be palindromes
        if x < 0:
            return False

        x_string = str(x)
        n = len(x_string)

        # Step backward using -1 as the step
        for i, j in zip(range(0, n // 2), range(-1, -n - 1, -1)): # Only doing half as other half should be the same if palindrome 
            if x_string[i] != x_string[j]:
                return False

        return True
        
        
