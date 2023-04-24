from random import choice, random
from time import perf_counter
from queue import Queue
from copy import copy


def tabuSimulation(graph, nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMax, getInitialSolution, maxTime):
    """
    Function to compute simulation in order to find an approach solution of the best graph partition in nbClasses while using tabu (without aspiration) algorithm.
    """
    startTime = perf_counter()
    timeLeft = maxTime

    bestSolution = None
    bestValue = sum([e.weight for e in graph.edges]) # We take at maximum the sum of the weight of the edges of 'graph'

    while timeLeft >= 0:
        randomSolution = getInitialSolution(graph, nbClasses, equityMax) # Meets the criterion of fairness by definition
        newSolution, newValue = tabu(graph, nbClasses, equityMax, randomSolution, neighborhoodFunction, tabuListSize, nbIterMax, timeLeft)
        if newValue < bestValue:
            bestSolution = copy(newSolution)
            bestValue = newValue

        timeLeft = maxTime - (perf_counter() - startTime)

    totalTime = perf_counter() - startTime

    return bestSolution, bestValue, totalTime


def findBestSolution(graph, nbClasses, equityMax, neighborhoodFunction, currentSolution, currentValue, tabuList):
    """
    Function to compute the best solution among the neighbors of 'currentSolution' with value 'currentValue' not in 'tabuList'
    using 'neighborhoodFunction' with 'nbClasses' and 'equityMax' in graph 'graph'.
    """
    neighbors = neighborhoodFunction(graph, currentSolution, currentValue, nbClasses, equityMax, random = False, getMovement = True) # All the neighbors and their associated movement
    bestValue = sum([e.weight for e in graph.edges])
    bestSolution = None
    reverseMovement = None
    for neighbor, neighborValue, movement in neighbors:
        if neighborValue < bestValue and movement not in tabuList.queue: # '.queue' attributes allows to iterate on the queue
            bestSolution = copy(neighbor)
            bestValue = neighborValue
            reverseMovement = (movement[0], currentSolution[movement[0]]) # With movement[0] the index of the vertex that change is class
    if bestSolution == None: # The size of the tabu list is too greater compared to the number of vertices of 'graph' (and the number of classes)
        # We choose a random neighbor
        bestSolution, bestValue, movement = list(neighborhoodFunction(graph, currentSolution, currentValue, nbClasses, equityMax, random = True, getMovement = True))[0] # list[0] as the function returns a generator
        reverseMovement = (movement[0], currentSolution[movement[0]])
    return bestSolution, bestValue, reverseMovement


def tabu(graph, nbClasses, equityMax, initialSolution, neighborhoodFunction, tabuListSize, nbIterMax, timeLeft):
    """
    Function to compute an approach solution of the best graph partition in nbClasses using tabu (without aspiration) algorithm.
    """
    startTime = perf_counter()
    currentSolution = initialSolution
    bestSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)
    bestValue = currentValue
    tabuList = Queue() # i.e. FIFO list
    nbIter = 0
    while nbIter < nbIterMax and (perf_counter() - startTime) <= timeLeft: # We also check the left time
        nbIter += 1
        newSolution, newValue, reverseMovement = findBestSolution(graph, nbClasses, equityMax, neighborhoodFunction, currentSolution, currentValue, tabuList)
        if newValue < bestValue:
            bestSolution = copy(newSolution)
            bestValue = newValue
        if newValue >= currentValue: # Improvement : we only make 'tabu' the 'currentSolution' only if 'newSolution' is better.
            tabuList.put(reverseMovement)
            if tabuList.qsize() > tabuListSize:
                tabuList.get() # remove the first element come in the queue.
        currentSolution = copy(newSolution)
        currentValue = newValue

    return bestSolution, bestValue




































#
