Sol1: straightforward recursive solution
the max avg of `A[0:] = avg(A[0:i]) + rev(A[i:], K-1) loops from 1...len(A) - K + 1`

Sol2: from the conception of recursion, we can get the idea of dp
`dp[i, k]` means the max avg of dividing the array `A[i:]` into at most `k` parts
return: `dp(0, K)`
init: `dp(i:0...len(A) - 1, 1) = sum(A[i:])/len(A[i:])`
equation: `dp(i, k) = max(dp(j, k-1) + avg(A[i, j] loops j:i+1...N-k+2`