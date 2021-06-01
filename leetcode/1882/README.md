### tl;dr

[Link to problem statement.](https://leetcode.com/problems/process-tasks-using-servers/)

### Idea

Using two heaps, `free` and `busy`, to monitor server status and select server wisely. When adding a server to a heap, prioritize as follow: `server_time > server_weight > server_index`. At the beginning, all servers are in `free` and their time is `0`.  
For each task:
- `time_now = task_index`
- Pop all `busy` servers if they are now free: `server_time <= time_now`
- Set their time to `0` to prioritize their weight later then push to `free`
- If no servers are free, pop the top `busy` as it is the soonest to be free.
- Pop the top `free`.
- Set it to process current task: `server_time += task_time`, then push to `busy`

### Complexity

with `n = number_of_servers, m = number_of_tasks`:
- time: `O(m * log(n))`
- space: `O(n)`
