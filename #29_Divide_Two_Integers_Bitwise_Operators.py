class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constants for 32-bit signed integer limits
        MAX_INT = 2147483647      # 2^31 - 1
        MIN_INT = -2147483648     # -2^31

        # 1. Handle the single 32-bit overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 2. Determine sign of the result
        # True if one is negative and the other is positive
        is_negative = (dividend < 0) ^ (divisor < 0)

        # 3. Work with absolute values
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        # 4. Exponential subtraction using bit shifts
        while a >= b:
            current_divisor = b
            multiple = 1
            
            # Double current_divisor until it exceeds remainder 'a'
            while a >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            
            # Subtract chunk and accumulate quotient
            a -= current_divisor
            quotient += multiple

        # 5. Apply sign
        if is_negative:
            quotient = -quotient

        # 6. Clamp within 32-bit bounds
        return max(MIN_INT, min(MAX_INT, quotient))
