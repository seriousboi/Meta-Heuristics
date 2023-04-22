from parsers import *
from structures import *
from checker import *
from exhaustive import *
from neighborhoods import *
from simulatedAnnealing import *
from gradients import *
# from tests import *


nbClasses = 2
equityMax = 2
maxTime = 15 #temps max en secondes
initialTemperature = 1000
MU = 0.99
nbChangeTemperature = 50
nbIterMaxFunction = lambda n : n**2 / 2 # with n the size of our problem.

filenames = [
'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt'
]

def testSimulatedAnnealing(nbClasses, equityMax, neighborhoodFunction, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime):

    print(f"Simulated annealing with {nbClasses} classes: \n")

    shutdownTemperature = 1000 * MU**nbChangeTemperature
    g = lambda T: MU * T # Positive decreasing function

    for filename in filenames:
        graph = loadGraph("data/"+filename)
        print(filename)

        nbIterMax = nbIterMaxFunction(len(graph.vertices))
        simulatedAnnealingSolution, simulatedAnnealingValue, timeTaken = simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, \
        initialTemperature, shutdownTemperature, g, nbIterMax, maxTime)

        print(f"Cost: {simulatedAnnealingValue}")
        print(f"Time: {timeTaken} seconds")
        print(simulatedAnnealingSolution)

        # Just as a precaution
        if not checkSolution(simulatedAnnealingSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ \n")

        print('\n')

# testExhaustive(nbClasses, equityMax, maxTime)
# testGradient(nbClasses, equityMax, swapNeighborhood, maxTime)
testSimulatedAnnealing(nbClasses, equityMax, randomPickNDropNeighborhood, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime)
