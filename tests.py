from parsers import loadGraph
from structures import Graph
from checker import checkSolution
from exhaustive import exhaustiveSearch
from gradients import gradient
from neighborhoods import *
from initialSolution import *
from randomSolution import getRandomSolution
from simulatedAnnealing import simulatedAnnealingSimulation
from tabu import tabuSimulation
from implicit import implicitSearch
from optimums import optimums
import pandas as pd

folder = "data"

filenames = ['dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt',
#'milleSommets.txt','dixMilleSommets.txt'
]

goodFilenames = ['dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt',]



def testEverything(maxTime,startStep = 0):
    step = 0
    nbClasses = 3
    results = []
    successPrctLeniency = 2 #pourcentage de tolérance avec la meilleure valeur pour considérer la recherche comme un succès
    successLeniency = (100+successPrctLeniency)/100

    for nbClasses in [2,4,6,8]:
        for filename in filenames:

            if step >= startStep:
                graph = loadGraph(f"{folder}/{filename}")
                print("instance",filename)
                print(graph.nbVertices, "vertices to split in",nbClasses,"classes")

                gradSwapValue,gradPnDValue,SAValue,tabuValue = testAllMethodsOnInstance(graph,nbClasses,maxTime)

                best = min(gradSwapValue,gradPnDValue,SAValue,tabuValue)
                gradSwapSuccess = int(gradSwapValue/best <= successLeniency)
                gradPnDSuccess = int(gradPnDValue/best <= successLeniency)
                SASuccess = int(SAValue/best <= successLeniency)
                tabuSuccess = int(tabuValue/best <= successLeniency)

                results += [[filename,graph.nbVertices,nbClasses,gradSwapValue,gradPnDValue,SAValue,tabuValue,gradSwapSuccess,gradPnDSuccess,SASuccess,tabuSuccess]]

                print(step+1,"steps done")
                print()

            step += 1

    resultsDF = pd.DataFrame(results,columns=["Instance","Sommets","Classes","Valeur gardient swap","Valeur gradient PnD","Valeur recuit simulé","Valeur méthode tabou","Succès gardient swap","Succès gradient PnD","Succès recuit simulé","Succès méthode tabou"])
    print(resultsDF)
    resultsDF.to_csv("results.csv", sep=';')

def testForSuccess(maxTime,startStep = 0):
    step = 0
    nbClasses = 2


    for filename in goodFilenames:

        if step >= startStep and filename in optimums[nbClasses]:
            graph = loadGraph(f"{folder}/{filename}")
            print("instance",filename)
            print(graph.nbVertices, "vertices to split in",nbClasses,"classes")

            gradSwapValue,gradPnDValue,SAValue,tabuValue = testAllMethodsOnInstance(graph,nbClasses,maxTime)

            optimum = optimums[nbClasses][filename]
            gradSwapSuccess = gradSwapValue/optimum <= successLeniency
            gradPnDSuccess = gradPnDValue/optimum <= successLeniency
            SASuccess = SAValue/optimum <= successLeniency
            tabuSuccess = tabuValue/optimum <= successLeniency

            print(gradSwapSuccess,gradPnDSuccess,SASuccess,tabuSuccess)

            print(step+1,"steps done")
            print()

        step += 1

    pd.DataFrame(durationsDF,columns=["Usine"]+headsetsNames+["Heures Disponibles"])




def testAllMethodsOnInstance(graph,nbClasses,maxTime):
    equityMax = max(2,int((graph.nbVertices/nbClasses)/10)) #équité à 10% près de la taille d'une classe moyenne
    initialTemperature = None
    MU = 0.85
    nbChangeTemperature = 50
    nbIterMaxFunction = lambda n : n**2 / 2
    nbIterMax = nbIterMaxFunction(graph.nbVertices)
    tabuListSize = 7
    getInitialSolution = getRandomSolution
    g = lambda T: MU * T

    print("gradSwap")
    gradSwapSolution, gradSwapValue, gradSwapTimeTaken = gradient(graph, nbClasses, equityMax, swapNeighborhood, maxTime,4)
    print(gradSwapValue)

    print("gradPnD")
    gradPnDSolution, gradPnDValue, gradPnDTimeTaken = gradient(graph, nbClasses, equityMax, pickNDropNeighborhood, maxTime,4)
    print(gradPnDValue)

    print("SA")
    SASolution, SAValue, SATimeTaken = simulatedAnnealingSimulation(graph, nbClasses, equityMax, pickNDropNeighborhood, \
    initialTemperature, nbChangeTemperature, MU, g, nbIterMax, getInitialSolution, maxTime)
    print(SAValue)

    print("tabu")
    tabuSolution, tabuValue, tabuTimeTaken = tabuSimulation(graph, nbClasses, equityMax, pickNDropNeighborhood, tabuListSize, nbIterMax, getInitialSolution, maxTime)
    print(tabuValue)

    return gradSwapValue,gradPnDValue,SAValue,tabuValue



#fonction à utiliser une seule fois pour avoir les optimums
def getOptimums(maxTime):
    optimums = {}
    times = {}

    for nbClasses in [4,8]:
        optimums[nbClasses] = {}
        times[nbClasses] = {}

        for filename in goodFilenames:
            graph = loadGraph(f"{folder}/{filename}")
            equityMax = max(2,int((graph.nbVertices/nbClasses)/10))
            print("instance",filename)
            print(graph.nbVertices, "vertices to split in",nbClasses,"classes")

            implicitSolution, implicitValue, timeTaken, nbVisited = implicitSearch(graph, nbClasses, equityMax, maxTime)

            if timeTaken < maxTime:
                optimums[nbClasses][filename] = implicitValue
                times[nbClasses][filename] = timeTaken
            else:
                optimums[nbClasses][filename] = None
                times[nbClasses][filename] = maxTime

            print(optimums)
            print(times)
            print()

        if optimums[nbClasses][filename] == None:
            break



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
        print()



def testGradient(nbClasses, equityMax, neighborhoodFunction, maxTime, nbImprovToBreak = None, useBlocks = False):

    print(f"Gradient with {nbClasses} classes: \n")

    for filename in filenames:
        graph = loadGraph(f"{folder}/{filename}")
        print(filename)

        gradientSolution, gradientValue, timeTaken = gradient(graph, nbClasses, equityMax, neighborhoodFunction, maxTime, nbImprovToBreak)
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
