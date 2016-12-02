class Graph:

    def __init__(self):
        self.neighbor = {}
        self.node = {}

    def add_node(self, node):
        self.node[node] = None

    def add_edge(self, node, edge):
        try :                               #<Adds an edge to the specified node(e.g. 1 -> 2)
            self.neighbor[node].append(edge)
        except :
            self.neighbor[node] = []
            self.neighbor[node].append(edge)
        try :                               #< Makes sure the edges are connected to all the nodes
            self.neighbor[edge].append(node)#(e.g. 2 -> 1) without this node 1 would be connected to 2
        except :                            #but 2 wouldnt be connected to 1
            self.neighbor[edge] = []
            self.neighbor[edge].append(node)

    def neighbors(self, node):
        try :
            return self.neighbor[node]
        except :
            return []

    def breath_first(self, node):
        visited = []
        queue = [node]                             #queue is the first node(or node specified)
        while len(queue) > 0:
            node = queue.pop(0)                    #each value gets returned so it is not run again
            if node not in visited:
                visited.append(node)               #it is then put into the visisteed list if not already
                for edge in self.neighbor[node]:
                    if edge not in visited:
                        queue.append(edge)         #makes the next value to be run, one of the current             
        f = open("Question 14 Text File BFS", "w") #values edges(the first edge i think)
        for x in visited:
            f.write(str(x) + "\n")                 #outputs every nodde visited into a text file
        f.close()
        return visited

    def dfs_code(self, node, visited):
        visited.append(node)                          #appends first value to list visited. then gets then next value by using the edge 
        for edge in self.neighbor[node]:              #of the current value(this should automatically be the one to the left of it)
            if edge not in visited:                   #then runs the code again etc.
                visited = self.dfs_code(edge, visited)
        f = open("Question 14 Text File DFS", "w")
        for x in visited:
            f.write(str(x) + "\n")
        f.close()
        return visited

    def depth_first(self, node):                      #seperate function so you can tell it which node you want to start from
        return self.dfs_code(node, [])
        

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
    print(" ")
    print(g.breath_first(1))
    print(" ")
    print(g.depth_first(1))

