# Google OA

import sys
class Solution:
    def find_nearest_stores(self, stores, houses):
        stores.sort()

        ohouses = [i for i in houses]
        houses.sort()
        s, h = 0, 0
        hmap = {}
        while h < len(houses) and s < len(stores):
            c = stores[s] + 0.5 * (stores[s+1] - stores[s] if s+1 < len(stores) else sys.maxint)
            while h < len(houses) and houses[h] < c:
                hmap[houses[h]] = stores[s]
                h += 1
            s += 1
        return [hmap[i] for i in ohouses]


if __name__ == "__main__":
    obj = Solution()
    stores, houses = [4,18,9,23,12,5], [23,2,12,18,11,3,6,19]
    print(obj.find_nearest_stores(stores, houses)) 
