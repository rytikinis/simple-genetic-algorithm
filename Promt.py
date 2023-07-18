import AI

individual = AI.AI(AI.generateRandomGenetic())
geneticScore = 0
generation = 1

while geneticScore != 45:
    print("---Generation " + str(generation) + "---")
    print("Generated new AI gene:", individual.genetics)
    
    ai1, ai2, ai3, ai4 = AI.createNewGeneration(individual)
    
    print("Mutated the gene, kids: ")
    print(ai1.genetics)
    print(ai2.genetics)
    print(ai3.genetics)
    print(ai4.genetics)
    
    print("The best one is:", AI.selectTheBestOne([ai1, ai2, ai3, ai4]).genetics)
    
    individual = AI.selectTheBestOne([ai1, ai2, ai3, ai4])
    geneticScore =  AI.countPoints(AI.str2list(individual.genetics))
    print("Genetic score:", geneticScore)
    generation += 1