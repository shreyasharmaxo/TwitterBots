import matplotlib.pyplot as plt
import random
from geneticResponse import genConvo
from geneticResponse import retConvo
from ngram import templates

class enConvo:
    '''
    Class to generate a conversation as well as convert into an array.
    In the array, first index refers to type of response and format chosen
    Second index refers to the seed word used to generate the NEXT response.
    '''

    def __init__(self):
        '''
        initialized empty convoArray
        '''
        self.convoArray = []

    def firstConvo(self):
        '''
        adding a predefined initial conversation, where the first index is -1 to avoid confusion by the decoder
        '''
        firstConvo = [-1, 'Obama', -1, -1]
        self.convoArray.append(firstConvo)

    def addConvo(self):
        '''
        adding & generating responses based upon the previous second index
        '''
        convo = self.convoArray[-1]
        prevWord = convo[1]
        randInt = random.randint(0,len(templates) - 1)
        text = genConvo(randInt,prevWord)

        wordText = text.split(" ")
        nextConvoIndex = random.randint(0, len(wordText) -1)
        self.convoArray.append([randInt,text[nextConvoIndex],text])

    def getConvoArray(self):
        '''
        returns current state of convoArray
        '''
        return self.convoArray

def decode(convoArray):
    '''
    accepts a convoArray as input, and prints out the corresponding conversation
    :param converstation array needed to decode (seed of convo)
    :return decoded full array with text
    '''
    result = []
    for i in range(len(convoArray)):
        current = convoArray[i]
        if(current[0] == -1):
            result.append("What do you think of %s" % current[1])
        if(current[0] != -1):
            #TODO add verbs for decode
            decoded = retConvo(current[0],convoArray[i-1][1],current[2])
            result.append(decoded)
    return result

def evaluateFitness(convoArray):
    '''
    Manually prints out conversation for user input to assess fitness
    Two measures: context & grammar
    Average two measures
    :param conversation array
    :return fitness results
    '''
    results = decode(convoArray)
    total = 0.0

    for i in range(len(results)):
        print('\033[0m')
        print('\033[1m' + str(i) + " " + results[i])
        print('\033[0m')
        try:
            grammar = input("Does this sentence make sense? (1 - yes, 0 - no)")
        except:
            grammar = input("Does this sentence make sense? (1 - yes, 0 - no)")

        try:
            context = input("Does this sentence make sense in the given context of the sentence? (1 - yes, 0 - no)")
        except:
            context = input("Does this sentence make sense in the given context of the sentence? (1 - yes, 0 - no)")

        total = total + grammar + context

    return total/(len(results * 2))

def initialFitPopulation():
    '''
    first population of responses, only adding n responses with fitness > p
    :return: initial fit responses & fitness
    '''

    fitResponses = []
    totalFitness = 0.0
    while(len(fitResponses) < 5):
        test = enConvo()
        test.firstConvo()
        for i in range(3):
            test.addConvo()
        fitness = (evaluateFitness(test.getConvoArray()))
        print(fitness)
        if(fitness >= 0.60):
            totalFitness = totalFitness + fitness
            fitResponses.append(test.getConvoArray())
            print("added convo array: ")
            print(test.getConvoArray())
            print("added fitness: ")
            print(fitness)

    return fitResponses, totalFitness/len(fitResponses)

def mutate(convoSet):
    '''
    'randomly' combine a convoSet into one convo
    :param conversation set to mutate
    :return mutated conversation result
    '''
    result = []
    for i in range(len(convoSet[0])):
        randomMutate = random.randint(0,len(convoSet) - 1)
        result.append(convoSet[randomMutate][i])
    return result

def randomFitPopulation(convo):
    '''
    Use mutate to generate newer populations, only saving the best
    :param conversation set
    :return fit responses and average fitness
    '''
    fitResponses = []
    totalFitness = 0.0
    while(len(fitResponses) < 5):
        result = mutate(convo)
        fitness = evaluateFitness(result)
        print(fitness)
        print(" ")
        if(fitness >= 0.60):
            totalFitness = totalFitness + fitness
            fitResponses.append(result)
            print("added convo array: ")
            print(result)
            print("added fitness: ")
            print(fitness)

    return fitResponses, totalFitness/(len(fitResponses))

def geneticAlgo():
    '''
    Genetic Algorithm
    1. get first population
    2. mutate 10 times
    3. plot points
    '''
    fitnessResults = []
    fitResults = []
    randomFitConvo, avgFirstFit = initialFitPopulation()
    fitnessResults.append(avgFirstFit)

    fitResults = randomFitConvo

    for i in range(9):
        print(fitnessResults)
        print " "
        mutateResult, fitness = randomFitPopulation(fitResults)
        fitnessResults.append(fitness)
        fitResults = mutateResult

    plt.plot(fitnessResults)
    plt.show()

if __name__ == '__main__':
    geneticAlgo()