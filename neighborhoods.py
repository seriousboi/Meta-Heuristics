from copy import copy



def getSwapNeighborhood(solution):
    neighborhood = []

    #on fait une double boucle sur le tableau avec swapIndex1 < swapIndex2 pour éviter les symétries
    for swapIndex1 in range(len(solution)):
        for swapIndex2 in range(swapIndex1+1,len(solution)):

            if solution[swapIndex1] != solution[swapIndex2]:
                neighbor = copy(solution)

                temp = neighbor[swapIndex1]
                neighbor[swapIndex1] = neighbor[swapIndex2]
                neighbor[swapIndex2] = temp

                neighborhood += [neighbor]
    return neighborhood
