# First approach (String conversion)

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        s = str(n)
        maxProd = 0

        for i in range(len(s)):
            first_digit = int(s[i])

            for j in range(i+1,len(s)):
                second_digit = int(s[j])

                if (first_digit * second_digit) > maxProd:
                    maxProd = first_digit * second_digit

        return maxProd


# Second approach (Finding largest and second largest digits, and then multiplying them)

class Solution(object):
    def maxProduct(self, n):
      
        largest=0
        second_largest=0
      
        while(0<n):
            digits=n%10
          
            if(digits>largest):
                second_largest=largest
                largest=digits
              
            elif(digits>second_largest):
                second_largest=digits
              
            n//=10
          
        return largest*second_largest        
