from parsers import loadGraph
from structures import Graph
from checker import checkSolution
from exhaustive import exhaustiveSearch
from gradients import gradient, getRandomSolution
from simulatedAnnealing import simulatedAnnealingSimulation
from tabu import tabuSimulation
from implicit import implicitSearch
from optimums import *
from os import listdir

folder = "data"

filenames = [
'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt'
]

goodFilenames = ['dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt',]



def testEverything(maxTime,startStep = 0):
    step = 0

    for nbClasses in [2,4,8]:
        for filename in goodFilenames:

            if step >= startStep:
                graph = loadGraph(f"{folder}/{filename}")
                print("instance",filename)
                print(graph.nbVertices, "vertices to split in",nbClasses,"classes")

                print(testAllMethodsOnInstance(graph,nbClasses,maxTime))

                print(step+1,"steps done")
                print()

            step += 1



def testAllMethodsOnInstance(graph,nbClasses,maxTime):
    equityMax = max(2,int((graph.nbVertices/nbClasses)/10)) #équité à 10% près de la taille d'une classe moyenne

    gradientSolution,timeTaken = gradient(graph,nbClasses, neighborhoodFunction, maxTime, nbImprovToBreak)

    gradientSolution,timeTaken = gradient(graph,nbClasses, neighborhoodFunction, maxTime, nbImprovToBreak)

    simulatedAnnealingSolution, simulatedAnnealingValue, timeTaken = simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, \
    initialTemperature, shutdownTemperature, g, nbIterMax, maxTime)

    tabuSolution, tabuValue, timeTaken = tabuSimulation(graph, nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMax, maxTime)


    return 



def getOptimums(maxTime):
    optimums = {}
    times = {}

    for nbClasses in [2,4,8]:
        optimums[nbClasses] = {}
        times[nbClasses] = {}

        for filename in goodFilenames:
            graph = loadGraph(f"{folder}/{filename}")
            equityMax = max(2,int((graph.nbVertices/nbClasses)/10))
            print("instance",filename)
            print(graph.nbVertices, "vertices to split in",nbClasses,"classes")

            implicitSolution, implicitValue, timeTaken = implicitSearch(graph, nbClasses, equityMax, maxTime)

            if timeTaken < maxTime:
                optimums[nbClasses][filename] = implicitValue
                times[nbClasses][filename] = timeTaken
            else:
                optimums[nbClasses][filename] = None
                times[nbClasses][filename] = maxTime

            print(optimums)
            print(times)
            print()



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
    """
    Function to launch simulated annealing algorithm over the files.
    """
    print(f"Simulated annealing with {nbClasses} classes: \n")

    shutdownTemperature = 1000 * MU**nbChangeTemperature
    g = lambda T: MU * T # Positive decreasing function

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        nbIterMax = nbIterMaxFunction(graph.nbVertices)
        simulatedAnnealingSolution, simulatedAnnealingValue, timeTaken = simulatedAnnealingSimulation(graph, nbClasses, equityMax, neighborhoodFunction, \
        initialTemperature, shutdownTemperature, g, nbIterMax, maxTime)

        print(f"Cost: {simulatedAnnealingValue}")
        print(f"Time: {timeTaken} seconds")
        print(simulatedAnnealingSolution)

        # Just as a precaution
        if not checkSolution(simulatedAnnealingSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ \n")

        print('\n')



def testTabu(nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMaxFunction, maxTime):
    """
    Function to launch tabu search algorithm over the files.
    """
    print(f"Tabu with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        nbIterMax = nbIterMaxFunction(graph.nbVertices)
        tabuSolution, tabuValue, timeTaken = tabuSimulation(graph, nbClasses, equityMax, neighborhoodFunction, tabuListSize, nbIterMax, maxTime)

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
    print(f"Implicit with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        implicitSolution, implicitValue, timeTaken = implicitSearch(graph, nbClasses, equityMax, maxTime)

        print(f"Cost: {implicitValue}")
        print(f"Time: {timeTaken} seconds")
        print(implicitSolution)

        # Just as a precaution
        if not checkSolution(implicitSolution, nbClasses, True, equityMax):
            print("/!\ invalid solution /!\ \n")

        print('\n')
