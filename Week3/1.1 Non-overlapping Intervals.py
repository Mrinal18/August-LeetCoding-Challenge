
"""

Algorithm

The Greedy approach just discussed was based on choosing intervals greedily based on the starting points. But in this approach, we go for choosing points greedily based on the end points. For this, firstly we sort the given intervals based on the end points. Then, we traverse over the sorted intervals. While traversing, if there is no overlapping between the previous interval and the current interval, we need not remove any interval. But, if an overlap exists between the previous interval and the current interval, we always drop the current interval.

To explain how it works, again we consider every possible arrangement of the intervals.

Case 1:

The two intervals currently considered are non-overlapping:

In this case, we need not remove any interval and for the next iteration the current interval becomes the previous interval.

Case 2:

The two intervals currently considered are overlapping and the starting point of the later interval falls before the starting point of the previous interval:

In this case, as shown in the figure below, it is obvious that the later interval completely subsumes the previous interval. Hence, it is advantageous to remove the later interval so that we can get more range available to accommodate future intervals. Thus, previous interval remains unchanged and the current interval is updated.

Case 3:

The two intervals currently considered are overlapping and the starting point of the later interval falls before the starting point of the previous interval:

In this case, the only opposition to remove the current interval arises because it seems that more intervals could be accommodated by removing the previous interval in the range marked by AA. But that won't be possible as can be visualized with a case similar to Case 3a and 3b shown above. But, if we remove the current interval, we can save the range BB to accommodate further intervals. Thus, previous interval remains unchanged and the current interval is updated.

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end: 
                end = e
            else: 
                cnt += 1
        return cnt


