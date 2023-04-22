from structures import *

def loadGraph(filePath):
    file = open(filePath,"r")
    lines = file.readlines()
    for lineIndex in range(len(lines)):
        lines[lineIndex] = lines[lineIndex].split()
    file.close()

    nbVertices = int(lines[1][0])
    nbEdges = int(lines[1][1])

    vertices = []
    for vertexIndex in range(nbVertices):
        vertex = Vertex(vertexIndex,[],0)
        vertices += [vertex]

    edges = []
    for edgeIndex in range(nbEdges):
        start = vertices[int(lines[5+edgeIndex][0])-1]
        end = vertices[int(lines[5+edgeIndex][1])-1]
        weight = int(lines[5+edgeIndex][2])
        edge = Edge(edgeIndex,start,end,weight)
        edges += [edge]

        start.edges += [edge]
        start.degree += 1

        end.edges += [edge]
        end.degree += 1

    graph = Graph(vertices,edges,nbVertices,nbEdges)
    return graph
