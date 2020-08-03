"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #for this solution we will be checking from the mid, if the two halfs and the other reversed half is equal or not. 
        
        l , r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
       
        
    
    #OR simple. make everything lowercase, remove any alphanumeric symbols and check if this string is equal to the reverse of itself
        new_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return new_s  ==  new_s[::-1]
    
    
    
