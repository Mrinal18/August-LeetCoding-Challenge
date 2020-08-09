"""
Actually, we have already had a taste of in-place algorithm in the previous implementation of BFS, where we directly modified the input grid to mark the oranges that turn rotten, rather than using an additional visited table.

How about we apply the in-place algorithm again, but this time for the role of the queue variable in our previous BFS implementation?

The idea is that at each round of the BFS, we mark the cells to be visited in the input grid with a specific timestamp.

By round, we mean a snapshot in time where a group of oranges turns rotten.

Algorithm

In the above graph, we show how we manipulate the values in the input grid in-place in order to run the BFS traversal.

1). Starting from the beginning (with timestamp=2), the cells that are marked with the value 2 contain rotten oranges. From this moment on, we adopt a rule stating as "the cells that have the value of the current timestamp (i.e. 2) should be visited at this round of BFS.".

2). For each of the cell that is marked with the current timestamp, we then go on to mark its neighbor cells that hold a fresh orange with the next timestamp (i.e. timestamp += 1). This in-place modification serves the same purpose as the queue variable in the previous BFS implementation, which is to select the candidates to visit for the next round.

3). At this moment, we should have timestamp=3, and meanwhile we also have the cells to be visited at this round marked out. We then repeat the above step (2) until there is no more new candidates generated in the step (2) (i.e. the end of BFS traversal).

To summarize, the above algorithm is still a BFS traversal in a 2D grid. But rather than using a queue data structure to keep track of the visiting order, we applied an in-place algorithm to serve the same purpose as a queue in a more classic BFS implementation.

Time Complexity: O(N^2)
Space Complexity: O(1)

"""

class Solution(object):
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2
