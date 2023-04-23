from random import choice, random
from time import perf_counter
from math import exp, log


def simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, initialTemperature, nbChangeTemperature, \
MU, positiveDecreasingFunction, nbIterMax, getInitialSolution, maxTime):
    startTime = perf_counter()
    timeLeft = maxTime

    bestSolution = None
    bestValue = sum([e.weight for e in graph.edges]) # We take at maximum the sum of the weight of the edges of 'graph'

    while timeLeft >= 0:
        randomSolution = getInitialSolution(graph, nbClasses, equityMax) # Meets the criterion of fairness by definition
        newSolution, newValue = simulatedAnnealing(graph, nbClasses, equityMax, randomSolution, neighborhoodFunction, \
        initialTemperature, nbChangeTemperature, MU, positiveDecreasingFunction, nbIterMax, timeLeft)
        if newValue < bestValue:
            bestSolution = newSolution
            bestValue = newValue

        timeLeft = maxTime - (perf_counter() - startTime)

    totalTime = perf_counter() - startTime

    return bestSolution, bestValue, totalTime


def simulatedAnnealing(graph, nbClasses, equityMax, initialSolution, neighborhoodFunction, initialTemperature, nbChangeTemperature, MU, \
positiveDecreasingFunction, nbIterMax, timeLeft):
    """
    Function to compute an approach solution of the best graph partition in nbClasses while using simulated annealing algorithm.
    """
    startTime = perf_counter()
    currentSolution = initialSolution
    bestSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)
    bestValue = currentValue
    if initialTemperature == None:
        initialTemperature = computeInitialTemperature(graph, nbClasses, equityMax, currentSolution, currentValue, neighborhoodFunction, 0.65) # initialTemperature
    shutdownTemperature = initialTemperature * MU**nbChangeTemperature
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


def computeInitialTemperature(graph, nbClasses, equityMax, initialSolution, initialValue, neighborhoodFunction, acceptanceRate):
    """
    Function to compute initial temperature from 'acceptanceRate' for simulated annealing algorithm.
    """
    neighbors = neighborhoodFunction(graph, initialSolution, initialValue, nbClasses, equityMax, random = False) # All the neighbors
    n = 0
    fitnessGap = []
    neighbors = list(neighbors)
    while n < (0.1 * len(neighbors) or n < 5): # n > 5 to get some of them
        fitnessGap.append(initialValue - neighbors[n][1]) # neighborValue
        n += 1

    sumFitnessGap = sum(fitnessGap)
    if sumFitnessGap: # i.e. different from 0
        meanFitnessGap =  sumFitnessGap / len(fitnessGap)
        return - meanFitnessGap / log(acceptanceRate)
    else: # i.e. = 0
        return 1000












































#
