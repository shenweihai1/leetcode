

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = [], []
        cnt = 1
        for ele in nums:
            cnt *= ele
            l.append(cnt)
        
        cnt = 1
        for ele in nums[::-1]:
            cnt *= ele
            r.append(cnt)
        r = r[::-1]

        ans = []
        for idx in range(len(nums)):
            l_p = 1 if idx - 1 < 0 else l[idx - 1]
            r_p = 1 if idx + 1 > len(nums) - 1 else r[idx + 1]
            ans.append(l_p * r_p)
        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.productExceptSelf([1,2,3,4]))