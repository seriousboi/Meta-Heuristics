from copy import copy
from random import choice, shuffle
from checker import checkSolution


def swapNeighborhood(graph,solution,value):
    neighborhood = []

    #on fait une double boucle sur le tableau avec swapIndex1 < swapIndex2 pour éviter les symétries
    for swapIndex1 in range(len(solution)):
        for swapIndex2 in range(swapIndex1+1,len(solution)):

            if solution[swapIndex1] != solution[swapIndex2]:
                neighbor = copy(solution)

                temp = neighbor[swapIndex1]
                neighbor[swapIndex1] = neighbor[swapIndex2]
                neighbor[swapIndex2] = temp

                #on calcule le coût de la solution voisine en ne regardant que les changements sur les arretes des sommets swappés
                neighborValue = value
                class1 = solution[swapIndex1]
                class2 = solution[swapIndex2]

                #changements sur les arretes du sommet 1
                for edge in graph.vertices[swapIndex1].edges:
                    opppositeVertexIndex = getOppositeEndOfEdge(swapIndex1,edge).id

                    if opppositeVertexIndex != swapIndex2:
                        if neighbor[opppositeVertexIndex] == class1:
                            neighborValue += edge.weight
                        if neighbor[opppositeVertexIndex] == class2:
                            neighborValue -= edge.weight

                #changements sur les arretes du sommet 2
                for edge in graph.vertices[swapIndex2].edges:
                    opppositeVertexIndex = getOppositeEndOfEdge(swapIndex2,edge).id

                    if opppositeVertexIndex != swapIndex1:
                        if neighbor[opppositeVertexIndex] == class2:
                            neighborValue += edge.weight
                        if neighbor[opppositeVertexIndex] == class1:
                            neighborValue -= edge.weight

                #il n'y a pas besoin de vérifier la validité des voisins du voisinage swap pour ce problème
                yield neighbor,neighborValue


def randomPickNDropNeighborhood(graph, solution, value, nbClasses, equityMax):
    """
    Function to compute a random neighbor of a given solution using Pick'n'Drop.
    """
    vertices = [i for i in range(len(solution))]
    shuffle(vertices) # Randomly shuffle the vertices index in solution
    possible_classes = [i for i in range(nbClasses)] # All the classes
    for v in vertices:
        possible_classes_v = copy(possible_classes)
        possible_classes_v.remove(solution[v]) # All the POSSIBLE classes (i.e. without the current class of vertex 'v')
        shuffle(possible_classes_v) # Randomly shuffle the possible classes
        for c in possible_classes_v:
            neighbor = copy(solution)
            neighbor[v] = c
            if checkSolution(neighbor, nbClasses, False, equityMax):
                neighborValue = value
                for edge in graph.vertices[v].edges:
                    opppositeVertexIndex = getOppositeEndOfEdge(v, edge).id
                    if neighbor[opppositeVertexIndex] == solution[v]:
                        neighborValue += edge.weight
                    if neighbor[opppositeVertexIndex] == c:
                        neighborValue -= edge.weight
                return neighbor, neighborValue


def getOppositeEndOfEdge(vertexId,edge):
    if edge.start.id == vertexId:
        return edge.end
    else:
        return edge.start
