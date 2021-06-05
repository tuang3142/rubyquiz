### tl;dr

[Link to problem statement.](https://leetcode.com/problems/stone-game-iv/)


### Idea

I first came up with this dynamic programming solution:  
`dp[n][p]` is the result of player `p` going first at `n` stones.  
`p = 0` for Alice and `p = 1` for Bob. Alice wins if `dp[n][0] is True`  
After a player removes `i` stones: `dp[n][p] = dp[n - i][1 - p]`  
If there is just 1 result that favors Alice: `dp[n - 1][1-p] is True`, then she wins. Same for Bob.

```python
def winnerSquareGame(n):
    def sqr(n): return int(n ** 0.5)
    def square(n): return sqr(n) ** 2 == n

    dp = [[True, False] if square(i) else [-1, -1] for i in range(n + 1)]

    for i in range(n + 1):
        for p in range(2):
            if dp[i][p] != -1: continue
            win = True if p == 0 else False
            for j in range(1, sqr(i) + 1):
                if win == dp[i - j**2][1 - p]:
                    dp[i][p] = win
                    break
            if dp[i][p] == -1:
                dp[i][p] = not win
    return dp[n][0]
```

This code runs in $O(n * \sqrt n)$ but it's slow because of the `p` loop. A faster solution is below:

```python
def winnerSquareGame(n):
    def sqr(n): return int(n ** 0.5)
    dp = [False] * (n + 1)
    for i in range(n + 1):
        if dp[i]: continue
        j = 1
        while i + j * j <= n:
            dp[i + j * j] = True
            j += 1

    return dp[n]
```

The idea is so elegant that I have to write a README this long. Assuming Alice loses going first at `n`, then she wins going first at `n + i^2`  
`¯\_(ツ)_/¯`


### Complexity

- time: $O(n * \sqrt n)$
- space: $O(n)$
