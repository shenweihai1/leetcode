class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = {(0, 0): poured}
        for i in range(1, query_row + 1):
            for j in range(i + 1):
                l = 0 if j == 0 else max(dp[(i-1, j-1)]-1, 0) / 2
                r = 0 if j == i else max(dp[(i-1, j)]-1, 0) / 2
                
                dp[(i, j)] = l + r
        
        return min(1, dp[(query_row, query_glass)])