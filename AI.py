import random

#AI indviduals#

class AI():
    def __init__(self, genetics):
        self.genetics = genetics
    
#Generates random genetic#
def generateRandomGenetic():
    genetic = ""
    for a in range(5):
        genetic += str(random.randint(1, 9))
    return int(genetic)

#Counts points of genetic#
def countPoints(List):
    points = 0
    for num in List:
        points += int(num)
    return points

#Mutates genetic#
def mutate(genetic):
    for i in range(random.randint(1, 3)):
        gen = str(genetic)
        mutated_chromosome = random.randint(0, 4)
        gen = str2list(gen)
        gen[mutated_chromosome] = random.randint(1, 9)
        gen = list2str(gen)
    return int(gen)

#Converts string to list#
def str2list(string):
    List = []
    string = str(string)
    for char in string:
        List.append(char)
    return List

def list2str(List):
    string = ""
    for item in List:
        string += str(item)
    return string

def createNewGeneration(ai):
    #Orignal#
    ai1 = AI(ai.genetics)
    #Mutated#
    ai2 = AI(mutate(ai.genetics))
    ai3 = AI(mutate(ai.genetics))
    ai4 = AI(mutate(ai.genetics))

    return ai1, ai2, ai3, ai4

def selectTheBestOne(individuals):
    bestOne = None
    for individual in individuals:
        if not bestOne:
            bestOne = individual
        if countPoints(str2list(individual.genetics)) > countPoints(str2list(bestOne.genetics)):
            bestOne = individual
    return bestOne

AI(generateRandomGenetic())