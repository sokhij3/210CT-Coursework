GRAPH:
    __INIT__(self):
         neighbor <- {}
         node <- {}
    

    ADD_NODE(self,node):
         node[node] <- None
    

    ADD_EDGE(self,node,edge):
        try:
            neighbor[node].append(edge)
        except:
             neighbor[node] <- []
             neighbor[node].append(edge)
        try:                               
             neighbor[edge].append(node)
        except:                            
             neighbor[edge] <- []
             neighbor[edge].append(node)
    

    NEIGHBORS(self,node):
        try:
            return  neighbor[node]
        except :
            return []
    


