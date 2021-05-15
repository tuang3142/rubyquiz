[Link to original solution](https://leetcode.com/problems/minimum-interval-to-include-each-query/discuss/1186817/JavaC%2B%2BPython-Priority-Queue-Solution)

### ***Idea

The solution is written in python instead because ruby does not comes with a priority queue library

Sort the queries and the intervals increasingly.
For each query `num`, find all the intervals that fit, then push them to a priority queue.
Prioritize `[size, end]` of an interval, that is `[j - i + 1, j]`.
The first of the queue, that has smallest size, should be the answer.
Also, we need to pop all the unfit inteval in the queue.
Since the query is sorted, the inteval that does not fit a query should also not fit the next one.  This would keep the queue size small.
