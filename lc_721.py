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
        import collections        

        # (username, idx): emails
        idx_acts = {(es[0], idx): es[1:] for idx, es in enumerate(A)}
        uf = UnionFind(idx_acts.keys())
        
        # email => [(username, idx)]
        inv_acts = collections.defaultdict(list)
        for u, emails in idx_acts.items():
            [uf.union(u, e) for email in emails for e in inv_acts.get(email, [])]
            [inv_acts[email].append(u) for email in emails]

        # merge connected accounts
        # (username, idx): set([email])
        ans = collections.defaultdict(set)
        for u, es in idx_acts.items():
            ans[uf.find(u)] |= set(es)

        return [[k[0]] + sorted(list(v)) for k, v in ans.items()]