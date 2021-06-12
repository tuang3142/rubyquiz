### tl;dr

[Link to problem statement.](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/)


### Idea

First, loop thru every row of the pizza to make a cut.  
If the cut contain an apple, we continue operating on the newly created, smaller pizza.  
This seems dp for the fact that we can make use of the smaller pizza's result.  
Second, profit!  
Also, it's worth mentioning that to check "if the cut contain an apple", use prefix matrix sum  
or google how to use it.


### Complexity

let `n, m = size of the pizza`, `N = max(n, m)`  
- time: `O(k * N^3)`
- space: `O(k * N^2)`

