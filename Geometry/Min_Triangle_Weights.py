# A polygon can be divided into triangles, find the minimal cost (sum of edges) to arrange it. 

import sys
from math import sqrt
class Solution:
	
	def dist(self, p1,p2):
		x1,y1=p1
		x2,y2=p2
		return sqrt((x2-x1)*(x2-x1) + (y2-y1)* (y2-y1))
		
	def findMWT(self, vertices: List[Tuple[int]]) -> float:
		if not vertices:
			return 0 
		if len(vertices)<=2:
			return 0 
		def solve(vertices, i,j):
			if j-i<=1:
				return 0 
			cost = sys.maxsize 
			#k is the middle vertext between i and j
			for k in range(i+1, j):
				CostTriangle = self.dist(vertices[i],vertices[k]) + self.dist(vertices[k],vertices[j])+self.dist(vertices[i],vertices[j])
				# print(CostTriangle)
				cost =min(cost, CostTriangle+ solve(vertices,i, k)+solve(vertices,k,j))
			
			return cost 
		return solve(vertices, 0,len(vertices)-1)
