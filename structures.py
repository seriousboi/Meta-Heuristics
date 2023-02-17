


class Vertex():
    def __init__(self,id,edges,degree):
        self.id = id
        self.edges = edges
        self.degree = degree



class Edge():
    def __init__(self,id,start,end,weight):
        self.id = id
        self.start = start
        self.end = end
        self.weight = weight

    def print(self):
        print("Edge "+str(self.id)+", from V"+str(self.start.id)+" to V"+str(self.end.id)+", weight:",self.weight)



class Graph():
    def __init__(self,vertices,edges,nbVertices,nbEdges):
        self.vertices = vertices
        self.edges = edges
        self.nbVertices = nbVertices
        self.nbEdges = nbEdges

    def print(self):
        print(self.nbVertices,"Vertices",self.nbEdges,"Edges")
        for edge in self.edges:
            edge.print()

    def getValueFromSolution(self,solution):
        value = 0
        for edge in self.edges:
            if solution[edge.start.id] != solution[edge.end.id]:
                value += edge.weight
        return value
