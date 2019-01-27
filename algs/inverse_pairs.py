
class Solution:
    # time complexity: N * log(N)
    def InversePairs(self, nnums):
        _, ans = self.mergeSort(nnums)
        return ans % 1000000007

    def mergeSort(self, nnums):
        
        # base cases
        N = len(nnums)
        if N <= 1:
            return nnums, 0
        
        A, lans = self.mergeSort(nnums[:N//2])
        B, rans = self.mergeSort(nnums[N//2:])
        ans, ivsp = [], lans + rans 
        i, j = 0, 0
        while i < len(A) and j < len(B): 
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1 
            else:
                ans.append(B[j])
                j += 1
                ivsp += len(A) - i

        ans += A[i:]
        ans += B[j:]
        return ans, ivsp

        
if __name__ == "__main__":
    obj = Solution()
    A = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print(obj.InversePairs(A))
