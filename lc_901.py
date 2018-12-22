class StockSpanner(object):
    def __init__(self):
        self.history = []
        self.dp = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.history.append(price)
        l = len(self.history) - 1 - 1
        size = 1
        while l > -1:
            if price >= self.history[l]:
                size += self.dp[l]
                l -= self.dp[l]
            else:
                break
        self.dp.append(size)
        return size


ac = [100, 80, 60, 70, 60, 75, 85]
obj = StockSpanner()
for i in ac:
    print(obj.next(i))