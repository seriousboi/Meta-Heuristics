from neighborhoods import swapNeighborhood, pickNDropNeighborhood
from tests import testGradient, testExhaustive, testSimulatedAnnealing, testTabu, testImplicit
from initialSolution import getGradientSolution, getImplicitSolution
from randomSolution import getRandomSolution

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

# testExhaustive(nbClasses, equityMax, maxTime)
testGradient(nbClasses, equityMax, neighborhoodFunction, maxTime, nbImprovToBreak = None, useBlocks = False)
# testSimulatedAnnealing(nbClasses, equityMax, neighborhoodFunction, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, getInitialSolution, maxTime)
# testTabu(nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMaxFunction, getInitialSolution, maxTime)
# testImplicit(nbClasses, equityMax, maxTime)
