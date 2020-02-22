class UnionFind(object):
    def __init__(self, ns):  # nodes
        self.father = {n: n for n in ns}

    def union(self, u, v):
        self.father[self.find(u)] = self.find(v)

    def find(self, u):
        if u == self.father[u]:
            return u

        self.father[u] = self.find(self.father[u])
        return self.father[u]

class Solution:
    def accountsMerge(self, A):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # email:idx
        e_i = {email: index for index, p in enumerate(A) for email in p[1:]}
        # UF(emails)
        UF = UnionFind(e_i.keys())
        # union within same group
        {UF.union(p[i], p[i + 1])  for p in A for i in range(1, len(p[1:]))}
        
        # merge into index:emails
        import collections
        ans = collections.defaultdict(set)
        
        for p in A:
            ans[e_i[UF.find(p[1])]] |= set(p[1:])
            
        return [[A[k][0]] + sorted(list(v)) for k, v in ans.items()]
