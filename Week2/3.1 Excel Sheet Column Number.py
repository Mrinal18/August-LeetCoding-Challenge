"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 70
"""


"""
This is using LEFT to RIGHT approch.

Scanning AZZC from right to left while accumulating results:

First, ask the question, what the value of 'C' is:
'C' = 3 x 260 = 3 x 1 = 3
result = 0 + 3 = 3
Then, ask the question, what the value of 'Z*' is:
'Z*' = 26 x 261 = 26 x 26 = 676
result = 3 + 676 = 679
Then, ask the question, what the value of 'Z**' is:
'Z**' = 26 x 262 = 26 x 676 = 17576
result = 679 + 17576 = 18255
Finally, ask the question, what the value of 'A***' is:
'A***' = 1 x 263 = 1 x 17576 = 17576
result = 18255 + 17576 = 35831


Algorithm

1. To get indices of alphabets, create a mapping of alphabets and their corresponding values. (1-indexed)
2. Initialize an accumulator variable result.
3. Starting from right to left, calculate the value of the character associated with its position and add it to result.
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        
        res = 0
        
        #convert into a hashmap for all the chars 
        
        dic = {chr(i+65): i +1 for i in range(26)}
        
        n = len(s)
        
        for i in range(n):
            curr = s[n - i - 1]
            res += (dic[curr] * (26 ** i))
            
        return res 

