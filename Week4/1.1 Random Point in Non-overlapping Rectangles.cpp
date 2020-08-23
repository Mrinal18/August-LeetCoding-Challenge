/*
Intuition

Some rectangles may be more likely to be sampled from than others, since some may contain more points than others, and each point has an equal chance of being sampled. Is there a way to select a rectangle to sample from, such that the probabilities are proportional to the number of points contained in each rectangle? Is there a way to do this using less than O(\text{total number of points})O(total number of points) space?

Algorithm

Create a weight array ww, where w[i]w[i] is the number of points in \text{rects}[i]rects[i].

Compute the prefix sum array pp, where p[x] = \sum_{i=0}^{x}w[i]p[x]=∑ i=0x​	w[i]
Generate a random integer \text{targ}targ in the range [0, \sum_{i=0}^{n}w[i]][0,∑i=0nw[i]], where \sum_{i=0}^{n}w[i]∑i=0 n​	w[i] is the total number of points in all rectangles.

Use binary search to find the index xx where xx is the lowest index such that \text{targ} < p[x]targ<p[x]. \text{rects}[x]rects[x] is the rectangle that we will sample from.

Note that for some index ii, all integers vv where p[i] - w[i] \leq v < p[i]p[i]−w[i]≤v<p[i] map to this index. Therefore, rectangles will be sampled proportionally to the rectangle weights.

The only step remaining is to choose a random point in \text{rects}[x]rects[x]. Generating random \text{x\_coordinate}x_coordinate and \text{y\_coordinate}y_coordinate within this rectangle area will suffice, but we can also reuse \text{targ}targ by mapping it to the point

\text{x\_coordinate} = x1 + (\text{targ}-p[i]+w[i]) \% (x2-x1+1) \\ \text{y\_coordinate} = y1 + (\text{targ}-p[i]+w[i]) / (x2-x1+1)x_coordinate=x1+(targ−p[i]+w[i])%(x2−x1+1)
y_coordinate=y1+(targ−p[i]+w[i])/(x2−x1+1)

This strategy is useful when calls to the random number generator are expensive.

Targ_To_Point
Mapping from targ to x_coordinate and y_coordinate for rects = [[1, 1, 2, 4], [3, 2, 5, 4], [2, 5, 5,
*/

class Solution {
public:

    vector<vector<int>> rects;
    vector<int> psum;
    int tot = 0;
    //c++11 random integer generation
    mt19937 rng{random_device{}()};
    uniform_int_distribution<int> uni;

    Solution(vector<vector<int>> rects) {
        this->rects = rects;
        for (auto& x : rects) {
            tot += (x[2] - x[0] + 1) * (x[3] - x[1] + 1);
            psum.push_back(tot);
        }
        uni = uniform_int_distribution<int>{0, tot - 1};
    }

    vector<int> pick() {
        int targ = uni(rng);

        int lo = 0;
        int hi = rects.size() - 1;
        while (lo != hi) {
            int mid = (lo + hi) / 2;
            if (targ >= psum[mid]) lo = mid + 1;
            else hi = mid;
        }

        auto& x = rects[lo];
        int width = x[2] - x[0] + 1;
        int height = x[3] - x[1] + 1;
        int base = psum[lo] - width * height;
        return {x[0] + (targ - base) % width, x[1] + (targ - base) / width};
    }
};
