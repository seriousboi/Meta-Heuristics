from structures import *
from parsers import *
from exhaustive import *



graph = loadGraph("data/vingtSommets.txt")
optimalSolution = exhaustiveSearch(graph)
print(optimalSolution)
print(graph.getValueFromSolution(optimalSolution))
#push test
