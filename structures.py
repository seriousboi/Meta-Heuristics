


class Vertex():
    def __init__(self,id,edges,neighbors,degree):
        self.id = id
        self.edges = edges
        self.neighbors = neighbors
        self.degree = degree



class Edge():
    def __init__(self,id,start,end,weight):
        self.id = id
        self.start = start
        self.end = end
        self.weight = weight



class Graph():
    def __init__(self,vertices,edges,nbVertices,nbEdges):
        self.vertices = vertices
        self.edges = edges
        self.nbVertices = nbVertices
        self.nbEdges = nbEdges
