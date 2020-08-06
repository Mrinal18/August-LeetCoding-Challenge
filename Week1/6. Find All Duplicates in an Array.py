"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Solution 1:
        if the number is there in dictionary then we append it to the list, which means that there are more than 1 elements for that number. else we just add it in the dictionary.
        """
        
        dup = {}
        res = []
        
        
        for i in nums:
            if i in dup:
                res.append(i)
            else:
                dup[i] = 1
                
        return res
        
        
        
        """
        Solution 2: 
        The elements are between1 and N and N is the size of the array. Therefore we can implicitly map an element to an index i.e. 1 maps to index 0, 2 maps to index 1, ...N maps to index N-1
Say for example that the number 4 appears twice. 4 implies index 3. We know that there are no negative numbers in the array. How about I mark the number at index 3 as negative when I first encounter 4. Now at the next occurence of 4, I will find the position implied by it (i.e. number at index 3) as negative. This means that 4 is a duplicate!
Make sure you use the abs(x)-1 to select the index implied by x. That is because, in a previous iteration, the position of x might have been marked negative
        """
        res = []
        
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] = -1*nums[abs(x) - 1]
            
        return res
        
    
