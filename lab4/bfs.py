
class Graph:
    def __init__(self,ver):
        self.nv = ver
        self.adj={}
        for n in range (self.nv):
            self.adj[n]=[]
            
    def addEdge(self,src,des): 
        self.adj[src].append(des) 

    def BFS(self, s): 
        self.visited = [] 
        queue = []  
        queue.append(s) 
        self.visited.append(s) 
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.adj[s]: 
                if i not in self.visited: 
                    queue.append(i) 
                    self.visited.append(i) 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3)  
g.BFS(2)  
