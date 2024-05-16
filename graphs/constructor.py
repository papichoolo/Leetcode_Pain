class Graph:
    def __init__(self):
        self.graph = {}
    def add_vert(self,value):
        if value not in self.graph.keys():
            self.graph[value]=[]
            return True
        return False