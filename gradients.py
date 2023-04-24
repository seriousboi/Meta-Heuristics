from random import choice
from time import perf_counter
from randomSolution import getRandomSolution
from math import floor


def gradient(graph, nbClasses, equityMax, neighborhoodFunction, maxTime, nbImprovToBreak = None, useBlocks = False):
    startTime = perf_counter()
    timeLeft = maxTime

    bestSolution = None
    bestValue = 1000000000

    while timeLeft >= 0:
        randomSolution = getRandomSolution(graph, nbClasses)
        newSolution, newValue = gradientDescent(graph, nbClasses, equityMax, randomSolution, neighborhoodFunction, nbImprovToBreak, useBlocks)

        if newValue < bestValue:

            bestSolution = newSolution
            bestValue = newValue

        timeLeft = maxTime - (perf_counter() - startTime)

    totalTime = perf_counter() - startTime

    return bestSolution, bestValue, totalTime


def gradientDescent(graph, nbClasses, equityMax, initialSolution, neighborhoodFunction, nbImprovToBreak, useBlocks):
    currentSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)

    #on fait des itérations jusqu'à ce que le voisinage n'ai pas de solution améliorante
    valueCanImprove = True
    while valueCanImprove:

        newSolution, newValue = gradientIterarion(graph, nbClasses, equityMax, currentSolution, neighborhoodFunction, nbImprovToBreak, usedBlock = None)

        if newValue < currentValue:
            currentSolution = newSolution
            currentValue = newValue
        else:
            valueCanImprove = False

    return currentSolution, currentValue


def findNbBlocks(nbNeighbors):
    """
    Function to find the maximal number of similar blocks for split neighborhood of a solution in gradient algorithm.
    The function compute the greater divider of a number different from itself.
    """
    nbBlocks = 1
    for x in range(floor(nbNeighbors) / 2, 2, -1):
        if nbNeighbors % x == 0:
            nbBlocks = x
            break

    return nbBlocks


def gradientIterarion(graph, nbClasses, equityMax, currentSolution, neighborhoodFunction, nbImprovToBreak, usedBlock):
    """
    Function to find one of the best value of neighborhood of a solution (depending of used criterion).
    """
    currentValue = graph.getValueFromSolution(currentSolution)

    # nombre de fois qu'on a trouvé une solution améliorante (relativement à la valeur initiale)
    nbImprov = 0
    initialValue = currentValue

    # le type de voisinage est modulable dans les paramètres
    neighborhood = list(neighborhoodFunction(graph, currentSolution, initialValue, nbClasses, equityMax))
    nbNeighbors = len(neighborhood)

    # utilisation des blocs
    if usedBlock != None:
        nbBlocks = findNbBlocks(nbNeighbors)
        nbSolPerBlock = int(nbNeighbors / nbBlocks)
        nbSol = nbSolPerBlock * usedBlock
    else:
        nbSolPerBlock = nbNeighbors

    nbSol = 0

    for neighbor, neighborValue in neighborhood:
        while nbSol < nbSolPerBlock:
            # on incrémente le compteur d'améliorations
            if  neighborValue < initialValue:
                nbImprov += 1

            # on change la solution courrante si la nouvelle est meilleure
            if neighborValue < currentValue:
                currentSolution = neighbor
                currentValue = neighborValue

            # on sort de l'itération si on a atteint le nombre d'améliorations voulues
            if nbImprovToBreak != None and nbImprov == nbImprovToBreak:
                return currentSolution, currentValue
            nbSol += 1


    return currentSolution, currentValue
