from parsers import *
from exhaustive import *
from neighborhoods import *
from gradients import *



filenames = [
'quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt'
]



def testExhaustive(nbClasses,maxIterations = None):
    global filenames

    if maxIterations == None:
        maxIterations = len(filenames)

    print("Exhaustive search,",nbClasses," classes:")
    for step in range(maxIterations):
        filename = filenames[step]

        graph = loadGraph("data/"+filename)
        print(filename)

        exhaustiveSolution = exhaustiveSearch(graph)
        print(graph.getValueFromSolution(exhaustiveSolution))
        print(exhaustiveSolution)
        print()



def testGradient(nbClasses,neighborhoodFunction,maxTime,nbImprovToBreak = None):
    global filenames

    print("Greedy gradient,",nbClasses," classes:")

    for filename in filenames:
        graph = loadGraph("data/"+filename)
        print(filename)

        gradientSolution = gradient(graph,nbClasses,swapNeighborhood,maxTime,nbImprovToBreak)
        print("Gradient:",graph.getValueFromSolution(gradientSolution))
        print(gradientSolution)
        print()
