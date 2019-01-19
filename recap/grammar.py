#-*- coding:utf-8
print(ord('a')) # 97
print(chr(97)) # 'a'

# order dictionary
# OrderedDict：保持插入时候的顺序，更新不改变顺序xx
cd = {23: 1, 42: 1, 11: -1, 2.5:1, -1:4}
od = collections.OrderedDict(sorted(cd.items(), key=lambda x:x[0]))
print(od) # OrderedDict([(-1, 4), (2.5, 1), (11, -1), (23, 1), (42, 1)])

# 26位整数表示字母
mask |= 1 << (ord(w) - ord('a'))   # 设置某位为1

# 1, 0 交换
1 ^ 1 = 0
0 ^ 1 = 1

ac = [1, 2, 4]
bisect.insort(ac, 2.4)
print(ac)  # [1, 2, 2.4, 4]

# all values true
l = [1, 3, 4, 5]
print(all(l))
# all values false
l = [0, False]
print(all(l))
# one false value
l = [1, 3, 4, 0]
print(all(l))
# one true value
l = [0, False, 5]
print(all(l))
# empty iterable
l = []
print(all(l))

# sort two columns
ans = [(1, 2), (1, 1), (-1, 2)]
ans = sorted(ans, key=lambda x: (-x[1], -x[0]))
print(ans)  # [(1, 2), (-1, 2), (1, 1)]

# total sorting
from itertools import permutations
mc = [1, 2, 3]
print(list(permutations(mc)))  # # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import combinations
mc = [1, 2, 3]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(sum([(list(combinations(mc, i))) for i in range(len(mc) + 1)], []))

import random
print(random.randint(1, 3)) # a <= N <= b

import bisect
ac = [1, 1, 2, 3]
# 遇到相同选最左边
# 遇到相同数字插在该数字的左边
print(bisect.bisect_left(ac, 2.9))  # 3
print(bisect.bisect_left(ac, 3)) # 3
print(bisect.bisect_left(ac, 3.1)) # 4
print(bisect.bisect_left(ac, 0.9))  # 0
print(bisect.bisect_left(ac, 1)) # 0
print(bisect.bisect_left(ac, 1.1)) # 2

from collections import Counter
a = [1, 2, 3, 1, 1, 2]
print(Counter(a))  # Counter({1: 3, 2: 2, 3: 1})

# 推导式
a = [1, 2, 3]
b = [2, 3, 4]
print([(i, j) for i in a for j in b if i > 1 and j > 2])  # [(2, 3), (2, 4), (3, 3), (3, 4)]

# find the most frequent element
A = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(A), key=A.count)) # count if the function

# map
ac = [(1, 2), [2, 3]]
print(map(list, ac))  # [[1, 2], [2, 3]]
print(map(lambda x: x[1], ac)) # [2, 3]

# filter 
ac = xrange(-5, 5)
print(filter(lambda x: x >= 0, ac))  # [0, 1, 2, 3, 4]

ac = [1, 2, 3]
bc = [2, 3, 4]
print(dict(zip(ac, bc)))  # {1: 2, 2: 3, 3: 4}

# 列表展开
A = [[1, 2], [3, 4, 5], [5, 6]]
print(sum(A, []))  # [1, 2, 3, 4, 5, 5, 6]
print([c for l in A for c in l if c > 1])  # [2, 3, 4, 5, 6]

# using lambda
pow = lambda x: x ** 2
print(pow(8)) # 64

# 操作集合
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # set([1, 2, 3, 4, 5])
print(A & B)  # set([3])
print(A - B)  # set([1, 2])
print(B - A)  # set([4, 5])

# 操作计数
import collections
A = collections.Counter([1, 2, 2])
B = collections.Counter([1, 2, 2, 4, 5, 2, 4])
# cnt <= 0 直接会去除
print(A + B)  # Counter({2: 5, 1: 2, 4: 2, 5: 1})
print(B - A)  # Counter({4: 2, 2: 1, 5: 1})

# 比较重要的一个, 排序字典
A = dict(("%s" % x, x) for x in range(5))
print A  # {'1': 'v', '0': 'v', '3': 'v', '2': 'v', '4': 'v'}
A = collections.OrderedDict(("%s" % x, "v") for x in range(3, 10))
A['0'] = 'v'  # 保持插入时候的顺序
A['4'] = 'v'  # 更新的话不会改变顺序
print(A)  # OrderedDict([('0', 'v'), ('1', 'v'), ('2', 'v'), ('3', 'v'), ('4', 'v')])