from neighborhoods import *



def gradient(graph,initialSolution,neighborhoodFunction,nbImprovToBreak = None):
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
    neighborhood = neighborhoodFunction(currentSolution)
    for neighbor in neighborhood:

        #les couts sont souvent recalculés, à améliorer
        neighborValue = graph.getValueFromSolution(neighbor)

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
