from parsers import *
from structures import *
from checker import *
from exhaustive import *
from neighborhoods import *
from gradients import *
from tests import *


nbClasses = 2
equityMax = 2
maxTime = 5 #temps max en secondes


testExhaustive(nbClasses,equityMax,maxTime)
testGradient(nbClasses,equityMax,swapNeighborhood,maxTime)
