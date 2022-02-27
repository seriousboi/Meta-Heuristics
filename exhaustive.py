from copy import copy



def exhaustiveSearch(graph):
    currentSolution = [0]*graph.nbVertices
    bestSolution = None
    bestValue = 1000000000
    partitionSize = graph.nbVertices//2

    finalArray = [1]*graph.nbVertices
    while currentSolution != finalArray:

        #sous optimal, on parcourt tout les mots binaires possibles
        getNextBinaryArray(currentSolution)

        #sous optimal, on recalcule la taille de la partition à chaque fois
        if getPartitionSize(currentSolution) == partitionSize:

            #sous optimal, on recalcule tout le coût à chaque fois
            currentValue = graph.getValueFromSolution(currentSolution)
            if currentValue < bestValue:

                #on utilise la bibliothèque copy pour faire une copie superficielle, sinon la copie change avec currentSolution
                bestSolution = copy(currentSolution)
                bestValue = currentValue

    return bestSolution



def getPartitionSize(binaryArray):
    partitionSize = 0
    for index in range(len(binaryArray)):
        partitionSize += binaryArray[index]
    return partitionSize



def getNextBinaryArray(binaryArray):
    for index in range(len(binaryArray)):

        if binaryArray[index] == 1:
            binaryArray[index] = 0
        else:
            binaryArray[index] = 1
            return
