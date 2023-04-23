from checker import checkSolution
from time import time
from copy import copy



def exhaustiveSearch(graph,nbClasses,maxTime):
    startTime = time()

    currentSolution = [0]*graph.nbVertices
    bestSolution = None
    bestValue = 1000000000

    finalArray = [nbClasses-1]*graph.nbVertices
    while currentSolution != finalArray:

        #sous optimal, on parcourt tout les mots binaires possibles
        nextSolution(currentSolution,nbClasses)

        #sous optimal, on recalcule la taille de la partition à chaque fois
        if checkSolution(currentSolution,nbClasses,False,2):

            #sous optimal, on recalcule tout le coût à chaque fois
            currentValue = graph.getValueFromSolution(currentSolution)
            if currentValue < bestValue:

                #on utilise la bibliothèque copy pour faire une copie superficielle, sinon la copie change avec currentSolution
                bestSolution = copy(currentSolution)
                bestValue = currentValue

        timeLeft = maxTime - (time() - startTime)
        if timeLeft <= 0:
            totalTime = time() - startTime
            return bestSolution,totalTime

    totalTime = time() - startTime
    return bestSolution,totalTime



def nextSolution(solution,nbClasses):
    for index in range(len(solution)):
        if solution[index] == nbClasses-1:
            solution[index] = 0
        else:
            solution[index] += 1
            return
