from time import perf_counter
from copy import copy
from itertools import product, filterfalse
from neighborhoods import getOppositeEndOfEdge

def computeValue(graph, lastSolution, lastValue, currentSolution):
    """
    Function to compute the value of a new solution from a old one and its value.
    """
    if lastSolution == None:
        return graph.getValueFromSolution(currentSolution)
    alreadyUpdate = {i : False for i in range(graph.nbEdges)}
    # alreadyUpdate = [False for i in range(graph.nbEdges)]
    # alreadyUpdate = {}
    newValue = lastValue
    for vertex in range(graph.nbVertices):
        if lastSolution[vertex] != currentSolution[vertex]:
            for edge in graph.vertices[vertex].edges:
                if not alreadyUpdate[edge.id]:
                # try:
                #     alreadyUpdate[edge.id] # The edge has already been met
                #     pass # We do nothing.
                # except KeyError: # The edge has never been met.
                    opppositeVertexIndex = getOppositeEndOfEdge(vertex, edge).id
                    if lastSolution[opppositeVertexIndex] != lastSolution[vertex] and currentSolution[opppositeVertexIndex] == currentSolution[vertex]:
                        newValue -= edge.weight
                    if lastSolution[opppositeVertexIndex] == lastSolution[vertex] and currentSolution[opppositeVertexIndex] != currentSolution[vertex]:
                        newValue += edge.weight
                    alreadyUpdate[edge.id] = True
                else: # delete the edge (save memory space) as we have already meet its two associated vertices
                    alreadyUpdate.pop(edge.id)

    return newValue


def implicitSearch(graph, nbClasses, equityMax, maxTime):
    """
    Function to compute the best graph partition in 'nbClasses'of 'graph' using implicit search in 'maxTime' with equity criterion 'equityMax'.
    """
    startTime = perf_counter()
    classes = [i for i in range(nbClasses)]

    if nbClasses != 2: # i.e. greater to 2

        def iteratorChecker(s):
            """
            Function to check if a solution generate by an iterator is valid.
            """
            min = graph.nbVertices
            max = 0
            for c in range(nbClasses):
                nbElements = s.count(c)
                if nbElements > max: max = nbElements
                if nbElements < min: min = nbElements
                if max - min > equityMax: return False

            return True

            solutions = filterfalse(lambda s : not iteratorChecker(s), product(range(nbClasses), repeat = graph.nbVertices))

    else: # Equals to 2
        if graph.nbVertices % 2 == 0: # i.e. an even number
            possibleValues = (int(graph.nbVertices / nbClasses), int((graph.nbVertices / nbClasses - 1)), int((graph.nbVertices / nbClasses + 1)))
        else: # An odd number
            possibleValues = (int((graph.nbVertices - 1) / nbClasses), int((graph.nbVertices - 1) / nbClasses + 1))
        solutions = filterfalse(lambda s : s.count(0) not in possibleValues, product(range(nbClasses), repeat = graph.nbVertices))

    bestSolution = None
    bestValue = 1000000000
    lastSolution = None
    lastValue = None

    for currentSolution in solutions:
        currentSolution = list(currentSolution)
        currentValue = computeValue(graph, lastSolution, lastValue, currentSolution)
        lastValue = currentValue
        if currentValue < bestValue:
            bestSolution = copy(currentSolution)
            bestValue = currentValue
        lastSolution = copy(currentSolution)
        timeLeft = maxTime - (perf_counter() - startTime)
        if timeLeft <= 0:
            totalTime = perf_counter() - startTime
            return bestSolution, bestValue, totalTime


    totalTime = perf_counter() - startTime
    return bestSolution, bestValue, totalTime
