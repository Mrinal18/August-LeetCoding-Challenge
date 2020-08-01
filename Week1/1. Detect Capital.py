"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        My initiuation: 
        1. if all the words are capital then true
        2. if first letter in string is capital and others are not then true 
        3. if all are lower then true
        4. else false 
        
        """
        
        
        if not word:
            return False
        
        #split the word
        
        if word.isupper():
            return True
        for i in range(1, len(word)):
            if word[i].isupper():
                print(word[i])
                return False
        if word[0].isupper():
            return True
        
        if word.islower():
            return True
        return False
            
            
        
