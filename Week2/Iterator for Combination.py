"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

"""

"""
Explanation Needs to be Updated
"""

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = k = combinationLength
        self.chars = characters
        
        # init the first combination
        self.nums = list(range(k))
        self.has_next = True
        
    def next(self) -> str:
        nums = self.nums
        n, k = self.n, self.k
        curr = [self.chars[j] for j in nums]
        
        # Generate next combination.
        # Find the first j such that nums[j] != n - k + j.
        # Increase nums[j] by one.
        j = k - 1
        while j >= 0 and nums[j] == n - k + j:
            j -= 1 
        nums[j] += 1
        
        if j >= 0:
            for i in range(j + 1, k):
                nums[i] = nums[j] + i - j
        else:
            self.has_next = False
        
        return ''.join(curr)
        
    def hasNext(self) -> bool:
        return self.has_next
