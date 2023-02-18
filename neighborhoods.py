from copy import copy



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

                class1 = solution[swapIndex1]
                class2 = solution[swapIndex2]
                neighborValue = value

                for edge in graph.vertices[swapIndex1].edges:
                    opppositeVertexIndex = getOppositeEndOfEdge(swapIndex1,edge).id

                    if opppositeVertexIndex != swapIndex2:
                        if neighbor[opppositeVertexIndex] == class1:
                            neighborValue += edge.weight
                        if neighbor[opppositeVertexIndex] == class2:
                            neighborValue -= edge.weight

                for edge in graph.vertices[swapIndex2].edges:
                    opppositeVertexIndex = getOppositeEndOfEdge(swapIndex2,edge).id

                    if opppositeVertexIndex != swapIndex1:
                        if neighbor[opppositeVertexIndex] == class2:
                            neighborValue += edge.weight
                        if neighbor[opppositeVertexIndex] == class1:
                            neighborValue -= edge.weight

                #il n'y a pas besoin de vérifier la validité des voisins du voisinage swap pour ce problème
                yield neighbor,neighborValue



def getOppositeEndOfEdge(vertexId,edge):
    if edge.start.id == vertexId:
        return edge.end
    else:
        return edge.start
