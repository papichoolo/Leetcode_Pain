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



bruh = Graph()
bruh.add_vert(1)
bruh.add_vert(2)
bruh.print_graph()