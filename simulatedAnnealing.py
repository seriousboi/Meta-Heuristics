from gradients import getRandomSolution
from random import choice, random
from time import perf_counter
from structures import *
from math import exp


def simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, initialTemperature, shutdownTemperature, positiveDecreasingFunction, nbIterMax, maxTime):
    startTime = perf_counter()
    timeLeft = maxTime

    bestSolution = None
    bestValue = sum([e.weight for e in graph.edges]) # We take at maximum the sum of the weight of the edges of 'graph'

    while timeLeft >= 0:
        randomSolution = getRandomSolution(graph.nbVertices, nbClasses) # Meets the criterion of fairness by definition
        newSolution, newValue = simulatedAnnealing(graph, nbClasses, equityMax, randomSolution, neighborhoodFunction, \
        initialTemperature, shutdownTemperature, positiveDecreasingFunction, nbIterMax, timeLeft)
        if newValue < bestValue:
            bestSolution = newSolution
            bestValue = newValue

        timeLeft = maxTime - (perf_counter() - startTime)

    totalTime = perf_counter() - startTime

    return bestSolution, bestValue, totalTime


def simulatedAnnealing(graph, nbClasses, equityMax, initialSolution, neighborhoodFunction, initialTemperature, shutdownTemperature, positiveDecreasingFunction, nbIterMax, timeLeft):
    """
    Function to compute an approach solution of the best graph partition in nbClasses while using simulated annealing algorithm.
    """
    startTime = perf_counter()
    currentSolution = initialSolution
    bestSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)
    bestValue = currentValue
    T = initialTemperature
    while T > shutdownTemperature:
        nbIter = 0
        while nbIter < nbIterMax and (perf_counter() - startTime) <= timeLeft: # We also check the left time
            newSolution, newValue = list(neighborhoodFunction(graph, currentSolution, currentValue, nbClasses, equityMax, random = True))[0]
            diff_values = newValue - currentValue
            if diff_values < 0:
                currentSolution = newSolution
                currentValue = newValue
                if currentValue < bestValue:
                    bestSolution = currentSolution
                    bestValue = currentValue
            else:
                p = random() # Random value between 0 and 1
                if p <= exp(- diff_values / T):
                    currentSolution = newSolution
                    currentValue = newValue
            nbIter += 1
        T = positiveDecreasingFunction(T)

    return bestSolution, bestValue
