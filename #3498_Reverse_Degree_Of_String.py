class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # I know ascii values of a is 97, and this can be done using ord('a'), same way z is 122
        #To make then into the value of straighforward alphabets, we'll do ord('a') - 96, then simply minus 27 and abs

        RevDeg = 0
        
        for i,char in enumerate(s):
            value = abs((ord(char) - 96) - 27)
            RevDeg += (i+1)*(value)

        return RevDeg

'''
Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.

'''
