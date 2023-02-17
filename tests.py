from parsers import *
from exhaustive import *
from neighborhoods import *
from gradients import *



filenames = ['quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
             'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
             'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt']



def runTests():
    global filenames

    for filename in filenames:
        graph = loadGraph("data/"+filename)
        print(filename)

        initialSolution = [0]*(graph.nbVertices - graph.nbVertices//2) + [1]*(graph.nbVertices//2)
        greedySolution = gradient(graph,initialSolution,swapNeighborhood)
        print("Greedy gradient:",graph.getValueFromSolution(greedySolution))
        print(greedySolution)

        exhaustiveSolution = exhaustiveSearch(graph)
        print("Exhaustive search:",graph.getValueFromSolution(exhaustiveSolution))
        print(exhaustiveSolution)

        print()
