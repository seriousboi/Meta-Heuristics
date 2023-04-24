from random import choice

def getRandomSolution(graph, nbClasses, equityMax = None, neighborhoodFunction = None, maxTime = None):
    verticesToAssign = [index for index in range(graph.nbVertices)]
    solution = [None] * graph.nbVertices

    for step in range(graph.nbVertices):
        classIndex = step % nbClasses
        vertexToAssign = choice(verticesToAssign)

        solution[vertexToAssign] = classIndex
        verticesToAssign.remove(vertexToAssign)

    return solution
