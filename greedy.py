from neighborhoods import *



def greedySearchSC(graph):
    #fonction shortcut qui appelle greedySearch avec la solution initiale où les n/2 premier sommets sont dans la même classe et le voisinage swap
    initialSolution = [0]*(graph.nbVertices - graph.nbVertices//2) + [1]*(graph.nbVertices//2)
    return greedySearch(graph,initialSolution,getSwapNeighborhood)



def greedySearch(graph,initialSolution,neighborhoodFunction):
    currentSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)

    #on fait des descentes tant que la soltution s'améliore
    valueCanImprove = True
    while valueCanImprove:

        currentSolution = greedyDescent(graph,currentSolution,neighborhoodFunction)
        newValue = graph.getValueFromSolution(currentSolution)

        if newValue < currentValue:
            currentValue = newValue
        else:
            valueCanImprove = False

    return currentSolution



def greedyDescent(graph,currentSolution,neighborhoodFunction):
    currentValue = graph.getValueFromSolution(currentSolution)

    #le type de voisinage est modulable dans les paramètres
    neighborhood = neighborhoodFunction(currentSolution)
    for neighbor in neighborhood:

        neighborValue = graph.getValueFromSolution(neighbor)
        if neighborValue < currentValue:
            currentSolution = neighbor
            currentValue = neighborValue

    return currentSolution
