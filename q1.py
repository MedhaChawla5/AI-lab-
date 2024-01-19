
class Graph:
	def __init__(self,ver):
		self.nv = ver
		self.adj = {}
		for n in range (self.nv):
			self.adj[n]=[]

	def add_edge(self,src,des):
		self.adj[src].append(des)


	def top_sort_util(self,visited , v , stack):
		visited[v] = True
		for i in self.adj[v]:
			if(visited[i]==False):
				self.top_sort_util(visited,i,stack)
		stack.append(v)

	def top_sort(self):
		visited = [False]*self.nv 
		stack = []

		for i in range(self.nv):
			if(visited[i]==False):
				self.top_sort_util(visited,i,stack)
		print(stack[::-1])

def main():
	n=6
	g = Graph(6)
	g.add_edge(5,2)
	g.add_edge(5,0)
	g.add_edge(2,3)
	g.add_edge(3,1)
	g.add_edge(4,1)
	g.add_edge(4,0)
	g.top_sort()

if __name__ =="__main__":
	main()

