from neighborhoods import swapNeighborhood, pickNDropNeighborhood
from tests import *

nbClasses = 2
equityMax = 2
maxTime = 5 #temps max en secondes
initialTemperature = 1000
MU = 0.99
nbChangeTemperature = 50
nbIterMaxFunction = lambda n : n**2 / 2 # with n the size of our problem.
tabuListSize = 7

#testExhaustive(nbClasses, equityMax, maxTime)
# testGradient(nbClasses, equityMax, swapNeighborhood, maxTime)
# testSimulatedAnnealing(nbClasses, equityMax, pickNDropNeighborhood, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime)
# testTabu(nbClasses, equityMax, pickNDropNeighborhood, tabuListSize, nbIterMaxFunction, maxTime)
# testImplicit(nbClasses, equityMax, maxTime)


getOptimums(300)
