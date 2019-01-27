
# Time complexity: N * N * (N - 1) * (N - 2) * ..... 1
class Solution:
    def premutations(self, A):
        ans = []
    
        def helper(idx):
            # base case for recursive function
            if idx == len(A):
                ans.append([k for k in A]) 
                return               

            for i in range(idx, len(A)):
                A[i], A[idx] = A[idx], A[i]
                helper(idx + 1)
                A[i], A[idx] = A[idx], A[i]
        
        helper(0)
        return ans

if __name__ == "__main__":  # Double quotation
    obj = Solution()
    A = [1, 2, 3] # 6
    print(obj.premutations(A))
