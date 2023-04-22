from parsers import loadGraph
from structures import Graph
from checker import checkSolution
from exhaustive import exhaustiveSearch
from gradients import gradient, getRandomSolution
from simulatedAnnealing import simulatedAnnealingSimulation
from os import listdir

# filenames = [
# 'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
# 'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
# 'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt'
# ]

folder = "data"
filenames = listdir(folder)

def testExhaustive(nbClasses,equityMax,maxTime = None,maxIterations = None):
    global filenames

    if maxIterations == None:
        maxIterations = len(filenames)

    print("Exhaustive search,",nbClasses,"classes:")
    print()
    for step in range(maxIterations):
        filename = filenames[step]

        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        exhaustiveSolution,timeTaken = exhaustiveSearch(graph,nbClasses,maxTime)
        if exhaustiveSolution == None:
            print("No solution found in",maxTime,"seconds")
        else:
            print("Cost:",graph.getValueFromSolution(exhaustiveSolution))
            print("Time:",timeTaken,"seconds")
            if timeTaken >= maxTime:
                print("Not finished")
            print(exhaustiveSolution)
            if not checkSolution(exhaustiveSolution,nbClasses,True,equityMax):
                print("/!\ invalid solution /!\ ")

        print()



def testGradient(nbClasses,equityMax,neighborhoodFunction,maxTime,nbImprovToBreak = None):
    global filenames

    print("Greedy gradient,",nbClasses,"classes:")
    print()

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        gradientSolution,timeTaken = gradient(graph,nbClasses, neighborhoodFunction, maxTime, nbImprovToBreak)
        print(f"Cost: {graph.getValueFromSolution(gradientSolution)}")
        print(f"Time: {timeTaken} seconds")
        print(gradientSolution)

        if not checkSolution(gradientSolution,nbClasses,True,equityMax):
            print("/!\ invalid solution /!\ ")
        print()


def testSimulatedAnnealing(nbClasses, equityMax, neighborhoodFunction, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, maxTime):

    print(f"Simulated annealing with {nbClasses} classes: \n")

    shutdownTemperature = 1000 * MU**nbChangeTemperature
    g = lambda T: MU * T # Positive decreasing function

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
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
