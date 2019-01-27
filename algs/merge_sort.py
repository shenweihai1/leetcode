#-*- coding:utf-8

class Solution:
    # time complexity: N * log(N)
    def mergeSort(self, nnums):
        def merge(A, B):
            ans = []
            i, j = 0, 0
            while i < len(A) and j < len(B): 
                if A[i] < B[j]:
                    ans.append(A[i])
                    i += 1 
                else:
                    ans.append(B[j])
                    j += 1

            ans += A[i:]
            ans += B[j:]
            return ans
        
        N = len(nnums)
        if N <= 1:
            return nnums
        
        l = self.mergeSort(nnums[:N//2])
        r = self.mergeSort(nnums[N//2:])
        return list(merge(l, r))

        
if __name__ == "__main__":
    obj = Solution()
    print(obj.mergeSort([1,2.1,31,4,5,6,7,0]))
