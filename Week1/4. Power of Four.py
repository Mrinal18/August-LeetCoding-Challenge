"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        
       
        #O(LOGN)
        if num == 0:
            return False
        while num %4 == 0:
            num /= 4
        
        
        return num == 1
       
        
        """
        Logrithmic solution
        
        we know that x = 4^a (where a is the power)
        log4(x) = a 
        a = 1/2 log2(x)
        
        here we just have to find a using math operations
        
        Time and Space complexity:
        O(1)
        """       
        return num > 0 and math.log2(num) % 2 == 0

        
        """
        Bit  manipulation
        
        
        """
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
        
        """
        Math + BitManipulation
        """
        
        
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1
            
