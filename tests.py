from parsers import loadGraph
from structures import Graph
from checker import checkSolution
from exhaustive import exhaustiveSearch
from gradients import gradient
from simulatedAnnealing import simulatedAnnealingSimulation
from tabu import tabuSimulation
from implicit import implicitSearch
from os import listdir

folder = "data"

filenames = [
'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt'
]

# filenames = listdir(folder)

def testExhaustive(nbClasses, equityMax, maxTime = None, maxIterations = None):

    if maxIterations == None:
        maxIterations = len(filenames)

    print(f"Exhaustive search with {nbClasses} classes: \n")

    for step in range(maxIterations):
        filename = filenames[step]

        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        exhaustiveSolution, exhaustiveValue, timeTaken, nbVisited = exhaustiveSearch(graph, nbClasses, maxTime)
        if exhaustiveSolution == None:
            print(f"No solution found in {maxTime} seconds.")
        else:
            print(f"Cost: {exhaustiveValue}")
            print(f"Time: {timeTaken} seconds")
            print(f"Number of solutions visited: {nbVisited}")
            if timeTaken >= maxTime:
                print("Not finished")
            print(exhaustiveSolution)
            if not checkSolution(exhaustiveSolution, nbClasses, True, equityMax):
                print("/!\ invalid solution /!\ ")

        print('\n')



def testGradient(nbClasses, equityMax, neighborhoodFunction, maxTime, nbImprovToBreak = None, useBlocks = False):

    print(f"Gradient with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        gradientSolution, gradientValue, timeTaken = gradient(graph, nbClasses, neighborhoodFunction, maxTime, nbImprovToBreak)
        print(f"Cost: {gradientValue}")
        print(f"Time: {timeTaken} seconds")
        print(gradientSolution)

        if not checkSolution(gradientSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ ")

        print('\n')


def testSimulatedAnnealing(nbClasses, equityMax, neighborhoodFunction, initialTemperature, nbChangeTemperature, MU, nbIterMaxFunction, getInitialSolution, maxTime):
    """
    Function to launch simulated annealing algorithm over the files.
    """
    print(f"Simulated annealing with {nbClasses} classes: \n")

    g = lambda T: MU * T # Positive decreasing function

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        nbIterMax = nbIterMaxFunction(graph.nbVertices)
        simulatedAnnealingSolution, simulatedAnnealingValue, timeTaken = simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, \
        initialTemperature, nbChangeTemperature, MU, g, nbIterMax, getInitialSolution, maxTime)

        print(f"Cost: {simulatedAnnealingValue}")
        print(f"Time: {timeTaken} seconds")
        print(simulatedAnnealingSolution)

        # Just as a precaution
        if not checkSolution(simulatedAnnealingSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ \n")

        print('\n')


def testTabu(nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMaxFunction, getInitialSolution, maxTime):
    """
    Function to launch tabu search algorithm over the files.
    """
    print(f"Tabu search with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        nbIterMax = nbIterMaxFunction(graph.nbVertices)
        tabuSolution, tabuValue, timeTaken = tabuSimulation(graph, nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMax, getInitialSolution, maxTime)

        print(f"Cost: {tabuValue}")
        print(f"Time: {timeTaken} seconds")
        print(tabuSolution)

        # Just as a precaution
        if not checkSolution(tabuSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ \n")

        print('\n')


def testImplicit(nbClasses, equityMax, maxTime):
    """
    Function to launch implicit search algorithm over the files.
    """
    print(f"Implicit search with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        implicitSolution, implicitValue, timeTaken, nbVisited = implicitSearch(graph, nbClasses, equityMax, maxTime)

        if implicitSolution == None:
            print(f"No solution found in {maxTime} seconds.")
        else:
            print(f"Cost: {implicitValue}")
            print(f"Time: {timeTaken} seconds")
            print(f"Number of solutions visited: {nbVisited}")
            if timeTaken >= maxTime:
                print("Not finished")
            print(implicitSolution)
            if not checkSolution(implicitSolution, nbClasses, True, equityMax):
                print("/!\ invalid solution /!\ ")

        print('\n')
