"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).


Solution:

One might argue that we could use the heap data structure (also known as PriorityQueue in Java) to maintain the list of coordinates. The elements in the heap data structure are ordered automatically, and this does eliminate the sorting operation. However, to maintain the elements in order, each insertion operation in heap would take \mathcal{O}(\log N)O(logN) time complexity. In other words, one can consider the heap data structure as another form of sorting, which amortizes the cost of sorting operating over each insertion.

One could apply the head data structure to replace the sorting operation here, which could make the code more concise. But this is not the main point here.

That being said, one thing that we can do is to reduce the scope of sorting, by partitioning the list of coordinates into subgroups based on the column index.


Although we would still need to sort the subgroups respectively, it would be faster to sort a series of subgroups than sorting them all together in a single group. Here is a not-so-rigid proof.

Suppose that we have a list of NN elements, it would then takeO(NlogN) time to sort this list.
Next, we divide the list into kk sublists equally. Each list would contain kN elements. Similarly, it would take O(kN .logkN) time to sort each sublist.

More importantly, another rationale to partition the list into column based groups is that this is also the format of results that are asked in the problem.

Once we sort the column based groups, we can directly return the groups as results, without the need for extraction as we did in the previous approach.

This is also the reason why we would not recommend to further partition the list based on the combination of <column, row> index. Although theoretically, the more groups that we partition the list into, the faster the sorting operations would be.

If we partition the list into the groups lead by <column row> index, we would need some additional processing to extract the results. Hence, it would become an overkill.

Algorithm

We could implement the above intuition based on the previous approaches. Again, we could break it down into 3 steps:

Step 1): First of all, we create a hashmap called columnTable with the column index as key and the list of <row, value> tuples as value. This hashmap is used to hold the groups of coordinates.

We traverse the input tree by either BFS or DFS. During the traversal, we populate the hashmap that we created above.

Meanwhile, we also note down the minimal and maximal column index during the traversal. The minimal and maximal column index defines the range of column index. With this range, we could iterate through columns in order without the need for sorting, as one will see later.

Step 2): Once we populate the above hashmap, we then sort the value in each entry of the hashmap, i.e. we sort each group of coordinates led by the column index.

Step 3): From the sorted hashmap, we extract the results that are grouped by the column index.

In the following, we give some sample implementations with both the BFS traversal and the DFS traversal.

BFS Traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return [] 
        
        
        
        columnHash = defaultdict(list)
        min_col = max_col = 0
        
        def BFS(root):
            nonlocal min_col, max_col
            queue = deque([(root, 0, 0)])
            
            while queue: 
                node, row, col = queue.popleft()
                
                if node is not None:
                    columnHash[col].append((row, node.val))
                    min_col = min(min_col, col)
                    
                    max_col = max(max_col, col)
                    
                    queue.append((node.left, row+1, col-1))
                    queue.append((node.right, row+1, col+1))
                    
            
        BFS(root)
        
        ret  = []
        
        for col in range(min_col, max_col+1):
            ret.append([val for row, val in sorted(columnHash[col])])
            
            
        return ret
        
        
