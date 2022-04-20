from parsers import *
from exhaustive import *
from neighborhoods import *
from greedy import *



filenames = ['quatreSommets.txt','cinqSommets.txt','dixSommets.txt','quinzeSommets.txt','dixSeptSommets.txt',
             'vingtSommets.txt','vingtEtunSommets.txt','vingtDeuxSommets.txt','vingtTroisSommets.txt','vingtQuatreSommets.txt','vingtCinqSommets.txt',
             'trenteSommets.txt','cinquanteSommets.txt','centSommets.txt','cinqCentSommets.txt','milleSommets.txt']



def runTests():
    global filenames

    for filename in filenames:
        graph = loadGraph("data/"+filename)
        print(filename)

        greedySolution = greedySearchSC(graph)
        print(greedySolution)
        print(graph.getValueFromSolution(greedySolution))

        exhaustiveSolution = exhaustiveSearch(graph)
        print(exhaustiveSolution)
        print(graph.getValueFromSolution(exhaustiveSolution))

        print()
