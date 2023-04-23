from math import floor

def f(neighborhood):
    nbBlocks = 1
    for x in range(floor(len(neighborhood) / 2), 2, -1):
        if len(neighborhood) % x == 0:
            nbBlocks = x
            break

    return nbBlocks

l = [0] * 15

print(f(l))
