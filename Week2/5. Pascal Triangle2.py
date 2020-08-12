"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]


"""

class Solution:
"""
    Intuition

Notice that in the previous approach, we have maintained the previous row in memory on the premise that we need terms from it to build the current row. This is true, but not wholly.

What we actually need, to generate a term in the current row, is just the two terms above it (present in the previous row).

Formally, in memory,

pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
where pascal[i][j] is the number in ith row and jth column of Pascal's triangle.

So, trying to compute pascal[i][j], only the memory regions of pascal[i-1][j-1] and pascal[i-1][j] are required to be accessed.

Algorithm

Let's take a step back and analyze the circumstances under which pascal[i][j] might be accessed. Given that we have already employed DP to save us valuable run-time, the access pattern for pascal[i][j] looks a bit like this:

WRITE pascal[i][j] (after generating it from pascal[i-1][j-1] and pascal[i-1][j])
READ pascal[i][j] to generate pascal[i+1][j]
READ pascal[i][j] to generate pascal[i+1][j+1]
That's it! Once we've written out pascal[i][j]:

We don't ever need to modify it.
It's only read a fixed number of times, i.e. twice (thanks to DP).
Hypothetically, if we kept the the current row (in the process of being generated) and the previous row, in the same memory block, what kind of access patterns would we see (assume pascal[j] means the jth number in a row)?

pascal[j] was somehow generated in a previous instance. Currently, it holds the previous row value.

pascal[j] (which holds the jth number of the previous row) must be read when writing out pascal[j] (the jth number of the current row).

Obviously they are the same memory location, so a conflict exists: the previous row value of pascal[j] will be lost after the write-out.
Is that ok? If we don't need to read the previous row value of pascal[j] anymore, is there any harm in writing out the current row value in its place?
pascal[j] (which holds the jth number of the previous row) must be read when writing out pascal[j+1] (the j+1th number of the current row). These are two different memory locations, so there is no conflict.

If we managed to keep all read accesses on the previous row value of pascal[j], before any write access to pascal[j] for the current row value, we should be good! That's possible by evaluating each row from the end, instead of the beginning. Thus, a new row value of pascal[j+1] must be generated before doing so for pascal[j].

The following animation demonstrates the above algorithm, used to generate the 4th row of Pascal's Triangle, from an existing 3rd row:


    """
    def getRow(self, rowIndex: int) -> List[int]:
        #lets make a dummy matrix only for the row given
        
        A = [1]*(rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                A[i-j] += A[i-j-1]
                
        return A
