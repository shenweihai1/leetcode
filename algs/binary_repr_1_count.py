#-*- coding:utf-8
# 计算一个数二进制中1的个数，负数使用补码，并且机器默认32-bit
"""
    比如-5的补码
    1. 原码是: 0000 0000 0000 0000 0000 0000 0000 0101
    2. 反码是: 1111 1111 1111 1111 1111 1111 1111 1010
    3. 反码加1即为补码: 1111 1111 1111 1111 1111 1111 1111 1011
    则其1的个数为31
"""

from ctypes import *
def count(num):
    cnt = 0
    flag = 1
    while c_int(flag).value:
        if c_int(num & flag).value:
            cnt += 1
        flag = flag << 1
    return cnt


if __name__ == "__main__":
    print count(-5)