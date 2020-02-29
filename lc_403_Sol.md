### Solution 1
`dp[steps][idx]`: 表示以步长steps是否可以跳到stones[idx]

`dp[steps][idx] = any(dp[steps - 1][j], dp[steps][j], dp[steps + 1][j]) where stones[j] + steps = stones[idx]`

init: `dp[1][1] = True`

return: `any(dp[:][len(stones) - 1])`

time complexity: `O(N * N)`

### Solution 2
`dp[idx]: 在位置idx，所有可能跳下一步的steps`

```
for steps in dp[idx]:
    if stones[idx] + steps == stones[-1]:
        return True
    
    update dp[j]  where stones[ j ] + steps = stones[ idx ]
```

init: `dp[0] = set([1])`

time complexity: worstest case is `O(N * N)`

space complexity: worstest case is `O(N * N)`

### Solution 3, recursive method
https://leetcode.com/problems/frog-jump/discuss/522990/Simple-Python-solution-with-lru_cache