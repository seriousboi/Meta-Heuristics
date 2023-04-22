from neighborhoods import swapNeighborhood, randomPickNDropNeighborhood
from tests import testGradient, testExhaustive, testSimulatedAnnealing

nbClasses = 2
equityMax = 2
maxTime = 5 #temps max en secondes
initialTemperature = 1000
MU = 0.99
nbChangeTemperature = 50
nbIterMaxFunction = lambda n : n**2 / 2 # with n the size of our problem.

# testExhaustive(nbClasses, equityMax, maxTime)
# testGradient(nbClasses, equityMax, swapNeighborhood, maxTime)
testSimulatedAnnealing(nbClasses, equityMax, randomPickNDropNeighborhood, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime)
