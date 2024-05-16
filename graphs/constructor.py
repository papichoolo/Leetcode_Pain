class Graph:
    def __init__(self):
        self.graph = {}
    def add_vert(self,value):
        if value not in self.graph.keys():
            self.graph[value]=[]
            return True
        return False
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex,":",self.graph[vertex])
    def add_edge(self,v1,v3):
        if v1 in self.graph.keys() and v3 in self.graph.keys():
            self.graph[v1].append(v3)
            self.graph[v3].append(v1)
            return True
        return False



bruh = Graph()
bruh.add_vert(1)
bruh.add_vert(2)
bruh.add_edge(2,1)
bruh.print_graph()