from neighborhoods import swapNeighborhood
from gradients import gradient
from implicit import implicitSearch


def getGradientSolution(graph, nbClasses, equityMax = None, neighborhoodFunction = swapNeighborhood, maxTime = 2):
    """
    Function to compute an initial solution using greedy gradient algorithm.
    """
    return gradient(graph, nbClasses, neighborhoodFunction, maxTime)[0]


def getImplicitSolution(graph, nbClasses, equityMax = 2, neighborhoodFunction = None, maxTime = 2):
    """
    Function to compute an initial solution using implicit search algorithm.
    """
    return implicitSearch(graph, nbClasses, equityMax, maxTime)[0]
