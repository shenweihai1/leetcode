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

### Set operation
reference: https://docs.python.org/2/library/sets.html

```
# set structure is implemented via hash
# init a set
u = set()
u = {2}
u = set([1, 2, 3])

# loop the set
for _ in u:
    pass

# check the existence
# time complexity nearly is O(1)
2 in u

# union
a = {3}
a | u
{2} | u
```
