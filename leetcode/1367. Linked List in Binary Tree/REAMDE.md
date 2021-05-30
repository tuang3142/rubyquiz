### tl;dr

[Link to the problem statement.](https://leetcode.com/problems/linked-list-in-binary-tree/)  
Given the root of a binary tree `root` and the head of a linked list `head`. Check if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree.

### Idea

This solution is similar to finding a pattern in a string. The brute force solution is acceptable. However, just like finding a string pattern, we can use the KMP algorithm to produce a faster solution. The idea is when checking a node, we don't need to start all over from the patern beginning.


### Complexity

with `n = depth_of_tree` and `k = length_of_link_list`:
- time: `O(n + k)`
- space: `O(k)` (we need to transform the linked list into and k-sized array, which makes me wonder why they gave the list at the first place but well, I don't hate the player)
