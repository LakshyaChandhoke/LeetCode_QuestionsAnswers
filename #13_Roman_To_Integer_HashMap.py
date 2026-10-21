class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)
        total = 0

        for i in range(0,n,+1):
            if i<n-1 and roman_table[s[i]] < roman_table[s[i+1]]:
                total = total - roman_table[s[i]]

            else:
                total = total + roman_table[s[i]]


        return total
