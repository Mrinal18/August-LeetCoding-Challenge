/*
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
*/

class Solution {
public:
    //This is normal BFS solution. 
    /*
    One of the most distinguished code patterns in BFS algorithms is that often we use a queue data structure to keep track of the candidates that we need to visit during the process.

The main algorithm is built around a loop iterating through the queue. At each iteration, we pop out an element from the head of the queue. Then we do some particular process with the popped element. More importantly, we then append neighbors of the popped element into the queue, to keep the BFS process running.
In the above implementations, we applied some tricks to further optimize both the time and space complexities.

Usually in BFS algorithms, we keep a visited table which records the visited candidates. The visited table helps us to avoid repetitive visits.

But as one notices, rather than using the visited table, we reuse the input grid to keep track of our visits, i.e. we were altering the status of the input grid in-place.

This in-place technique reduces the memory consumption of our algorithm. Also, it has a constant time complexity to check the current status (i.e. array access, grid[row][col]), rather than referring to the visited table which might be of constant time complexity as well (e.g. hash table) but in reality could be slower than array access.

We use a delimiter (i.e. (row=-1, col=-1)) in the queue to separate cells on different levels. In this way, we only need one queue for the iteration. As an alternative, one can create a queue for each level and alternate between the queues, though technically the initialization and the assignment of each queue could consume some extra time.

Complexity

Time Complexity: O(N), where NN is the size of the grid.

First, we scan the grid to find the initial values for the queue, which would take \mathcal{O}(N)O(N) time.

Then we run the BFS process on the queue, which in the worst case would enumerate all the cells in the grid once and only once. Therefore, it takes O(N) time.

Thus combining the above two steps, the overall time complexity would be O(N)+O(N)=O(N)

Space Complexity: O(N), where NN is the size of the grid.

In the worst case, the grid is filled with rotten oranges. As a result, the queue would be initialized with all the cells in the grid.

By the way, normally for BFS, the main space complexity lies in the process rather than the initialization. For instance, for a BFS traversal in a tree, at any given moment, the queue would hold no more than 2 levels of tree nodes. Therefore, the space complexity of BFS traversal in a tree would depend on the width of the input tree.

*/
   int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> rotten;
        int r = grid.size(), c = grid[0].size(), fresh = 0, t = 0;
        for(int i = 0;i < r; ++i){
            for(int j = 0; j < c; ++j){
                if(grid[i][j] == 2) rotten.push({i, j});
                else if(grid[i][j] == 1) fresh++;
                
            }
        }
        
        while(!rotten.empty()){
            int num = rotten.size();
            for(int i = 0; i < num; ++i){
                int x  = rotten.front().first, y = rotten.front().second;
                rotten.pop();
                if(x > 0 && grid[x-1][y] == 1){grid[x-1][y] =2; fresh--; rotten.push({x-1, y});};
                if(y > 0 && grid[x][y-1] == 1){grid[x][y-1] =2; fresh--; rotten.push({x, y-1});};
                if(x < r-1 && grid[x+1][y] == 1){grid[x+1][y] =2; fresh--; rotten.push({x+1, y});};
                if(y < c-1 && grid[x][y+1] == 1){grid[x][y+1] =2; fresh--; rotten.push({x, y+1});};
            }   
            if(!rotten.empty()) t++;
        }
        return (fresh == 0) ? t : -1;
    }
   
    
    
};
