
def maxSubArraySum(A): 
    cons = 0
    ans = min(A)
    for ele in A:
        cons = max(0, cons + ele)
        ans = max(ans, cons)
    return ans

   
# Driver function to check the above function  
A = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
A = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is: %s" % maxSubArraySum(A))
   