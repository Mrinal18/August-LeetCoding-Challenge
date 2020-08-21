"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

 class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #sort the list first 
        
        #Method 1
        #1. sort the list first. 
        #2. give a for roop to append all the even number first 
        #3. give a for loop for appending all the odd number
        #4. return the list 
        A.sort()
        
        if len(A) == 0:
            return []
        res = []
        for i in range(len(A)):
            if A[i] % 2 ==0:
                #means it is even
                res.append(A[i])
        for i in range(len(A)):
            if A[i] % 2 != 0:
                res.append(A[i])
                        
        
        return res
        
        
        #Method 2
        #1. take two variables start and end. 
        #2. while start is less than end, check if the number is odd
        #3. if it is odd, then swap the position of that index to the last one.
        
        i = 0
        j = len(A) - 1
        
        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                i -= 1
                j -= 1
            i += 1
        return A
