
class Graph:
	def __init__(self,ver):
		self.nv = ver
		self.adj = {}
		for n in range (self.nv):
			self.adj[n]=[]

	def add_edge(self,src,des):
		self.adj[src].append(des)

	def print_graph(self):
		for item in range (self.nv):
			print(item,"->",self.adj[item])

	def has_cycle_util(self,v,visited,stack):
		visited[v]= True
		stack[v]=True

		for i in self.adj[v]:
			if(visited[i]==False):
				if self.has_cycle_util(i,visited,stack):
					return True
			elif(stack[i]):
				return True
		stack[v]=False
		return False

	def has_cycle(self):
		visited=[False]*self.nv 
		stack = [False]*self.nv 

		for i in range(self.nv):
			if(visited[i]==False):
				if(self.has_cycle_util(i,visited,stack)):
					return True

		return False


def main():
	n=4
	g = Graph(4)
	g.add_edge(0,1)
	g.add_edge(0,2)
	g.add_edge(1,2)
	g.add_edge(2,0)
	g.add_edge(3,3)
	g.add_edge(2,3)
	g.print_graph()
	if g.has_cycle :
		print("The graph has cycle")
	else:
		print("No cycle")

if __name__ =="__main__":
	main()

