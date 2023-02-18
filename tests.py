from parsers import *
from structures import *
from checker import *
from exhaustive import *
from neighborhoods import *
from gradients import *



filenames = [
'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt'
]



def testExhaustive(nbClasses,equityMax,maxIterations = None):
    global filenames

    if maxIterations == None:
        maxIterations = len(filenames)

    print("Exhaustive search,",nbClasses," classes:")
    print()
    for step in range(maxIterations):
        filename = filenames[step]

        graph = loadGraph("data/"+filename)
        print(filename)

        exhaustiveSolution = exhaustiveSearch(graph)
        print("Cost",graph.getValueFromSolution(exhaustiveSolution))
        print(exhaustiveSolution)

        if not checkSolution(exhaustiveSolution,nbClasses,True,equityMax):
            print("/!\ invalid solution /!\ ")
        print()



def testGradient(nbClasses,equityMax,neighborhoodFunction,maxTime,nbImprovToBreak = None):
    global filenames

    print("Greedy gradient,",nbClasses," classes:")
    print()

    for filename in filenames:
        graph = loadGraph("data/"+filename)
        print(filename)

        gradientSolution = gradient(graph,nbClasses,swapNeighborhood,maxTime,nbImprovToBreak)
        print("Cost",graph.getValueFromSolution(gradientSolution))
        print(gradientSolution)

        if not checkSolution(gradientSolution,nbClasses,True,equityMax):
            print("/!\ invalid solution /!\ ")
        print()
