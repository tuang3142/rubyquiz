### tl;dr

[Link to problem statement.](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)


### Idea

Consider a string is constructed of 2 parts: `prefix + suffix`.  
The first operation is to swap `prefix` and `suffix`, eg: "11000" > "00011".  
Assume we already know the cost of turning those parts to binary strings,  
and do note that the binary can stars/ends with either `0` or `1`, we would have:
- `suffix0`: cost of turning suffix to binary ends with `0`
- `prefix0`: cost of turning prefix to binary starts with `0`

You can workout what `suffix1` and `prefix1` mean.  
So for each `prefix`, the cost of turning a whole string to binary should be:
- `suffix0` + `prefix1`, or
- `suffix1` + `prefix0`

### Complexity

with `n = len(string)`:
- time: `O(n)`
- space: `O(n)`
