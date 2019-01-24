#-*- coding:utf-8
"""
input: int[][] log = new int[n][3], log代表user可能在这个interval里任意时间点访问过这个网站:
@log[0]: user id;
@log[1]: start time;
@log[2]: end time;

问第k个访问网站的用户可能有哪些，返回他们的user id，顺序随意；
eg. log = [[1,20,30],[2,0,50],[3,45,70],[4,35,55]],
if(K==1) ----> return res=[1,2];
if(K==2) ----> return res=[1,2,3,4];
if(K==4) ----> return res=[2,3,4];. 

"""

def kthUser(logs, k):
    ans, must, possible = [], [], []
    for _, s, e in logs:
        ans.append(s)
        ans.append(e)
 
    ans = sorted(ans)
    for t in ans:
        cur_must, cur_possible = [], []
        for user_id, s, e in logs:
            if t >= e:
                cur_must.append(user_id)
            if s <= t < e:
                cur_possible.append(user_id)
            must.append(cur_must)
            possible.append(cur_possible)
 
    res = set()
    for idx, must_values in enumerate(must):
        if k - len(possible[idx]) <= len(must_values) < k:
            for i in possible[idx]:
                res.add(i)
 
    return list(res)
 
 
logs = [[1,20,30], [2,0,50], [3,45,70], [4,35,55]]
for k in [1, 2, 3, 4]:
    print "k = %s," % k, kthUser(logs, k)