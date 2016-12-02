#Q - Implement Dijkstra’s algorithm for a weighted graph data structure

#The graph i am using I found on google to make the implementation of dijkstras
#algorithm a bit easier.(The graph can be found on https://en.wikipedia.org/wiki/Dijkstra's_algorithm)

class Graph:

    def __init__(self):
        self.neighbor = {}
        self.node = {}

    def add_node(self, node):
        self.node[node] = None

    def add_edge(self, node, edge, weight):
        edgeWeight = {edge: weight}                #added weight by putting them in a seperate dictionary
        nodeWeight = {node: weight}                #with edges
        try:
            self.neighbor[node].append(edgeWeight) #make the node from the original dictionary = the new dictionary with weights
        except:
            self.neighbor[node] = []
            self.neighbor[node].append(edgeWeight)
        try:                               
            self.neighbor[edge].append(nodeWeight)
        except:                            
            self.neighbor[edge] = []
            self.neighbor[edge].append(nodeWeight)
        
    def neighbors(self, node):
        try:
            return self.neighbor[node]
        except:
            return []

    def dijkstras(self, initial):      #THIS CODE DOES NOT WORK
        visited = {initial: 0}
        current = initial
        path = {}
        nodes = set(self.node)
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break
            nodes.remove(min_node)
            current_weight = visited[min_node]
            for edge in self.neighbor[min_node]:
                weight = current_weight + self.neighbor[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
        return visited, path  


                    
if __name__ == "__main__":
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 6, 2)
    g.add_edge(3, 4, 11)
    g.add_edge(6, 5, 9)
    g.add_edge(4, 5, 6)
    
    print(g.neighbor)
    print(" ")
    print(g.node)
    print(" ")
    print(g.dijkstras(1, 5))
