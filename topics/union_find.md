
```
# Template for Union Find
class UnionFind(object):

    def __init__(self, N):
        self.father = {u: u for u in range(1, N + 1)}

    # O(1)
    def find(self, u):
        if u == self.father[u]: return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    # O(1)
    def union(self, u, v):
        self.father[u] = v
```


题目1: Connect graph
给定N个节点，初始节点相互独立, 实现函数
```
def connect(a, b): 将a, b两个节点连接
def query(a, b): 判断a, b是否连接, a -> c -> b return True
def query(a): 该节点所属集合个数
def query(): 当前集合个数
```

题目2: Minimum spanning tree

LeetCode: https://leetcode.com/problemset/all/?topicSlugs=union-find
`Leetcode`: Number of Islands
`Leetcode`: Graph Valid Tree
`Leetcode`: Accounts Merge
`Leetcode`: Redundant Connection