from copy import copy



def getSwapNeighborhood(binaryArray):
    neighborhood = []

    #on fait une double boucle sur le tableau avec swapIndex1 < swapIndex2 pour éviter les symétries
    for swapIndex1 in range(len(binaryArray)):
        for swapIndex2 in range(swapIndex1+1,len(binaryArray)):

            #ici on se sert du fait que on a que deux classes, si deux éléments du tableau sont différents on peut les échanger pour obtenir une solution dans le voisinage swap
            if binaryArray[swapIndex1] != binaryArray[swapIndex2]:
                neighbor = copy(binaryArray)

                temp = neighbor[swapIndex1]
                neighbor[swapIndex1] = neighbor[swapIndex2]
                neighbor[swapIndex2] = temp

                neighborhood += [neighbor]
    return neighborhood
