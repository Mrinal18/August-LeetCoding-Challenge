"""
952. Largest Component Size by Common Factor
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""


class Solution:
    """ slower than the enumeration of all factors ?! 
    """
    def largestComponentSize(self, A: List[int]) -> int:
        
        dsu = DisjointSetUnion(max(A))
        num_factor_map = {}
        
        for num in A:
            prime_factors = list(set(self.primeDecompose(num)))
            # map a number to its first prime factor
            num_factor_map[num] = prime_factors[0]
            # merge all groups that contain the prime factors.
            for i in range(0, len(prime_factors)-1):
                dsu.union(prime_factors[i], prime_factors[i+1])
        
        max_size = 0
        group_count = defaultdict(int)
        for num in A:
            group_id = dsu.find(num_factor_map[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id]) 
        
        return max_size


    def primeDecompose(self, num):
        """ decompose any positive number into 
                a series of prime factors.
            e.g. 12 = 2 * 2 * 3
        """
        factor = 2
        prime_factors = []
        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
            else:
                factor += 1
        prime_factors.append(num)
        return prime_factors


class DisjointSetUnion(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1] * (size+1)
    
    def find(self, x):
        """ return the component id that the element x belongs to. """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """ merge the two components that x, y belongs to respectively,
              and return the merged component id as the result.
        """
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.size[px] > self.size[py]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            px, py = py, px
        # add the smaller component to the larger one
        self.parent[px] = py
        self.size[py] += self.size[px]
        # return the final (merged) group
        return py
