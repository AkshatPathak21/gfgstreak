class Solution:
	def isEularCircuitExist(self, v, adj):
		#Code here
		return all(len(v_adj) % 2 == 0 for v_adj in adj)