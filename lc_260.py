#-*- coding:utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 0
        for i in nums:
            m ^= i    # 假设不相同的两个数字为p, q, 则该步骤等效于 p ^ q

        m = m - (m & (m - 1))  # m & (m - 1) 将二进制表示中最低位的1去掉, m - m & (m - 1)则表示为最低位1的二进制，其他位置全为0
        first, last = [], []
        for i in nums:
            (first if (i & m) == m else last).append(i)   # i & m == m, i相对应m的1的位置也是1
        m, n = 0, 0
        for i in first:
            m ^= i 
        for j in last:
            n ^= j
        return m, n