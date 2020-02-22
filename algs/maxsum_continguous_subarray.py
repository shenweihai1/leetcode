
def maxSubArraySumDP(A):
    dp = [A[0], A[0]]
    ans = A[0]
    for i in range(1, len(A) - 1):
        dp[i % 2] = dp[(i - 1) % 2] + A[i] if dp[(i - 1) % 2] >= 0 else A[i]
        ans = max(dp)
    return ans
   
# Driver function to check the above function  
A = [-13, -3, -25]
B = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is: %s" % maxSubArraySumDP(A))
print("Maximum contiguous sum is: %s" % maxSubArraySumDP(B))
   
