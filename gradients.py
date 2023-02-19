from neighborhoods import *
from random import choice
from time import time



def gradient(graph,nbClasses,neighborhoodFunction,maxTime,nbImprovToBreak = None):
    startTime = time()
    timeLeft = maxTime

    bestSolution = None
    bestValue = 1000000000

    while timeLeft >= 0:

        randomSolution = getRandomSolution(graph.nbVertices,nbClasses)
        newSolution = gradientDescent(graph,randomSolution,neighborhoodFunction,nbImprovToBreak)

        newValue = graph.getValueFromSolution(newSolution)
        if newValue < bestValue:

            bestSolution = newSolution
            bestValue = newValue

        timeLeft = maxTime - (time() - startTime)

    totalTime = time() - startTime
    
    return bestSolution,totalTime



def getRandomSolution(nbVertices,nbClasses):
    verticesToAssign = [index for index in range(nbVertices)]
    solution = [None]*nbVertices

    for step in range(nbVertices):
        classIndex = step%nbClasses
        vertexToAssign = choice(verticesToAssign)

        solution[vertexToAssign] = classIndex
        verticesToAssign.remove(vertexToAssign)

    return solution



def gradientDescent(graph,initialSolution,neighborhoodFunction,nbImprovToBreak):
    currentSolution = initialSolution
    currentValue = graph.getValueFromSolution(currentSolution)

    #on fait des itérations jusqu'à ce que le voisinage n'ai pas de solution améliorante
    valueCanImprove = True
    while valueCanImprove:

        currentSolution = gradientIterarion(graph,currentSolution,neighborhoodFunction,nbImprovToBreak)
        newValue = graph.getValueFromSolution(currentSolution)

        if newValue < currentValue:
            currentValue = newValue
        else:
            valueCanImprove = False

    return currentSolution



def gradientIterarion(graph,currentSolution,neighborhoodFunction,nbImprovToBreak):
    currentValue = graph.getValueFromSolution(currentSolution)

    #nombre de fois qu'on a trouvé une solution améliorante (relativement à la valeur initiale)
    nbImprov = 0
    initialValue = currentValue

    #le type de voisinage est modulable dans les paramètres
    neighborhood = neighborhoodFunction(graph,currentSolution,initialValue)
    for neighbor,neighborValue in neighborhood:

        #on incrémente le compteur d'améliorations
        if  neighborValue < initialValue:
            nbImprov += 1

        #on change la solution courrante si la nouvelle est meilleure
        if neighborValue < currentValue:
            currentSolution = neighbor
            currentValue = neighborValue

        #on sort de l'itération si on a atteint le nombre d'améliorations voulues
        if nbImprovToBreak != None and nbImprov == nbImprovToBreak:
            return currentSolution


    return currentSolution
