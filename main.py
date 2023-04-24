from neighborhoods import swapNeighborhood, pickNDropNeighborhood
from tests import *

nbClasses = 2
equityMax = 2
maxTime = 15 #temps max en secondes
initialTemperature = None
MU = 0.85
nbChangeTemperature = 50
nbIterMaxFunction = lambda n : n**2 / 2 # with n the size of our problem (or rather the number of vertices to assign).
tabuListSize = 7
neighborhoodFunction = swapNeighborhood # pickNDropNeighborhood
getInitialSolution = getGradientSolution

#testExhaustive(nbClasses, equityMax, maxTime)
# testGradient(nbClasses, equityMax, swapNeighborhood, maxTime)
# testSimulatedAnnealing(nbClasses, equityMax, pickNDropNeighborhood, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime)
# testTabu(nbClasses, equityMax, pickNDropNeighborhood, tabuListSize, nbIterMaxFunction, maxTime)
# testImplicit(nbClasses, equityMax, maxTime)


getOptimums(300)
