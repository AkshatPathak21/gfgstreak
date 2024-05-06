class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for a,b in edges:
            if a in self.graph_dict:
                self.graph_dict[a].append(b)
            else:
                self.graph_dict[a] = [b]
        print(self.graph_dict)

paths = [(1,2),(1,3),(1,4),(1,5)]

g = Graph(paths)