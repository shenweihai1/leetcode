#-*- coding:utf-8
"""
给一个String，表示时间，如“12:34”。. more info on 1point3acres
不用考虑corner cases, input一定是valid的。
要求只是用String中的四个数字，每个数字只用一次，产生一个新的时间(String)。
新时间是大于输入时间，但最靠近输入时间的时间点

直接全排序，然后校验是否正确时间格式， 如果正确再判断是否大于输入值，如果大于输入值取其中最小的，代码也比较简单
"""
from itertools import permutations
 
 
def rerange(input):
    nums = filter(lambda x: x.isdigit(), input)
    min_key = ":"  # ':' > digit
    for values in map(list, permutations(nums, len(nums))):
        if '0' <= values[0] <= '1' and '0' <= values[2] <= '5':
            key = values[0] + values[1] + ":" + values[2] + values[3]
            if key > input:
                min_key = min(key, min_key)
    return "-:-" if min_key == ":" else min_key
 
 
print rerange("12:34")
print rerange("12:37")
print rerange("09:30")