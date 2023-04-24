from tests import *

nbClasses = 2
equityMax = 2
maxTime = 2 #temps max en secondes
initialTemperature = None
MU = 0.85
nbChangeTemperature = 50
nbIterMaxFunction = lambda n : n**2 / 2 # with n the size of our problem (or rather the number of vertices to assign).
tabuListSize = 7
neighborhoodFunction = pickNDropNeighborhood # pickNDropNeighborhood
getInitialSolution = getRandomSolution

#testImplicit(nbClasses, equityMax, maxTime)
#testGradient(nbClasses, equityMax, swapNeighborhood, maxTime)
#testSimulatedAnnealing(nbClasses, equityMax, pickNDropNeighborhood, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction,getRandomSolution,maxTime)
#testTabu(nbClasses, equityMax, pickNDropNeighborhood, tabuListSize, nbIterMaxFunction,getRandomSolution,maxTime)


testEverything(maxTime)
