


def checkSolution(solution,nbClasses,verbose = False,equityMax = 2):
    #usage d'un dictionaire pour que les solutions ne soient pas contraintes à avoir des entiers de 0 à nbClasses-1 mais à simplement avoir nbClasses types d'éléments différents
    classCounts = {}

    #on compte le nombre d'occurence de chaque classe
    for classIndex in solution:

        if classIndex in classCounts:
            classCounts[classIndex] += 1
        else:
            classCounts[classIndex] = 1

    #on trouve les tailles maximale et minimale parmis les classes
    min = len(solution)
    max = 0
    for classIndex in classCounts:
        count = classCounts[classIndex]

        if count < min:
            min = count
        if count > max:
            max = count

    #on vérifie l'équité
    if not abs(max - min) <=  equityMax:
        if verbose:
            print("Equity not respected, difference between",min,"and",max,"is above",equityMax,"%")
        return False

    #on vérifie qu'il y a le bon nombre de classes
    nbActualClasses = len(classCounts)
    if nbActualClasses != nbClasses:
        if verbose:
            print("Incorrect number of classes,",nbActualClasses,"instead of",nbClasses)
        return False

    return True
