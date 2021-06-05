### tl;dr

[Link to problem statement.](https://leetcode.com/problems/shortest-path-in-a-hidden-grid/)  
It's hard simulating the test so I'm gonna skip it this time.


### Idea

Use dfs to draw the map, then bfs to calculate the shortest route.
First, initialize the map: `map[1000][1000]`. It's safe to assume the robot start at [500, 500] to avoid negative index when exploring. Then, do a dfs to draw out: 

- 0: empty cell (`robot.canMove is True`)
- 1: blocked, or hit wall (`robot.canMove is False`)
- 2: target cell (`robot.isTarget is True`)

The only trick is to backtrack the robot after a dfs recursion.

```python
robot.move(forward) # U D L R
dfs(robot)
robot.move(back)    # D U R L
```

Check if we can reach the target while `dfs`ing, then do a bfs to calculate the shortest path.

I tried to bfs right away and use `copy.deepcopy` to cheat out the backtracking, but it seemed to cost more both time and memory wise. Looks like this is foreseen by the author.


### Complexity

with `n * n` is the dimension of the map:
- time: `O(n^2)`
- space: `O(n^2)`
