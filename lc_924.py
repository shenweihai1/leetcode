
# https://buptwc.com/2018/10/15/Leetcode-924-Minimize-Malware-Spread/
class Solution(object):
 	def minMalwareSpread(self, graph, initial):

 		def dfs(node, vis):
 			for v in range(len(graph)):
 				if graph[node][v] == 1 and v not in vis:  
 					vis.add(v)
 					dfs(v, vis)

 		s_initial, t_vis = set(initial), set()
 		del_node, sub_len = min(initial), 0
 		for node in range(len(graph)):
 			if node not in t_vis:
 				vis = set([node])
 				dfs(node, vis)
 				infect = vis & s_initial
 				if len(infect) == 1:
 					if len(vis) > sub_len or (len(vis) == sub_len and min(list(infect)) < del_node):
 						del_node, sub_len = min(list(infect)), len(vis)
 				t_vis |= vis
 				
 		return del_node