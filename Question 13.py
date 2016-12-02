class Graph:

    def __init__(self):
        self.neighbor = {}
        self.node = {}

    def add_node(self, node):
        self.node[node] = None

    def add_edge(self, node, edge):
        try:                               #<Adds an edge to the specified node(e.g. 1 -> 2)
            self.neighbor[node].append(edge)
        except:
            self.neighbor[node] = []
            self.neighbor[node].append(edge)
        try:                               #< Makes sure the edges are connected to all the nodes
            self.neighbor[edge].append(node)#(e.g. 2 -> 1) without this node 1 would be connected to 2
        except:                            #but 2 wouldnt be connected to 1
            self.neighbor[edge] = []
            self.neighbor[edge].append(node)

    def neighbors(self, node):
        try:
            return self.neighbor[node]
        except:
            return []



if __name__ == "__main__":
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(4, 10)

    print(g.neighbor)

    
