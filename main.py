from structures import *
from parsers import *
from exhaustive import *
from neighborhoods import *
from greedy import *




graph = loadGraph("data/vingtSommets.txt")
solution = greedySearchSC(graph)
print(solution)
print(graph.getValueFromSolution(solution))
