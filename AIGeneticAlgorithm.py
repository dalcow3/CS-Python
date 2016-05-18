"""
File: HW2 Genetic Algorithm
Author: Chris Bruns
Description: Program that inputs a bit string to create an RGB value. Then
taking inputs regarding population and chromosomes creates a population that
will undergo mutations, selection, and crossovers as part of a genetic algorithm
to attempt to match the goal RGB value originally chosen.
"""

from math import *
import random
from random import *


def createPopulation(chromosomeNum):
    population = []
    count = 0
    while count < chromosomeNum:
        population.append(newBlood())
        count += 1
    return population

def newBlood():
    newBit = []
    count = 0
    while count < 24:
        num = str(randint(0,1))
        newBit.append(num)
        count += 1
    newBit = ''.join(newBit)
    return newBit

def createRGB(bit):
    red = bit[0:8]
    green = bit[8:16]
    blue = bit[16:24]
    return int(red, 2), int(green, 2), int(blue, 2)

def fitnessEquation(goalRGB, population):
    fitnessDict = {}
    red1 = (goalRGB[0])
    green1 = (goalRGB[1])
    blue1 = (goalRGB[2])
    bitWithFitness = []
    for element in population:
        key = element
        element = createRGB(element)
        red2 = (element[0])
        green2 = (element[1])
        blue2 = (element[2])
        unitsApart = sqrt(((red1 - red2)**2) + ((green1 - green2)**2) + ((blue1 - blue2)**2))
        fitnessDict[key] = unitsApart
        bitWithFitness = [[v, k] for k, v in fitnessDict.items()]
        bitWithFitness.sort()
    return bitWithFitness

def lotto(completeList):
    lottoList = []
    entryCount = len(completeList)
    listCount = 0
    while entryCount > 0:
        entry = completeList[listCount]
        count = entryCount
        while count > 0:
            lottoList.append(entry)
            count -= 1
        listCount += 1
        entryCount -= 1
    selection = choice(lottoList)
    return selection

def crossover(completeList):
    crossPoint = randint(1,23)
    parent1 = lotto(completeList)
    parent1 = parent1[1]
    parent1Front = parent1[0:crossPoint]
    parent1Back = parent1[crossPoint:24]
    parent2 = lotto(completeList)
    parent2 = parent2[1]
    parent2Front = parent2[0:crossPoint]
    parent2Back = parent2[crossPoint:24]
    firstNew = []
    firstNew.append(parent1Front)
    firstNew.append(parent2Back)
    secondNew = []
    secondNew.append(parent2Front)
    secondNew.append(parent1Back)
    joinFirst = ''.join(firstNew)
    joinSecond = ''.join(secondNew)
    return joinFirst, joinSecond          

def mutation(completeList):
    mutatedBin = lotto(completeList)
    mutatedBin = mutatedBin[1]
    position = randrange(len(mutatedBin))
    element = mutatedBin[position]
    if element == 1:
        element = str(0)
    else:
        element = str(1)
    return mutatedBin
       
def selection(completeList):
    selectionBin = lotto(completeList)
    completeList.remove(selectionBin)
    return selectionBin


def generation(inputRGB, populationList, chromosomeNum, selectionNum, mutationNum, newChromosome, crossoverPairs, generationCount):
    count = 0
    goalRGB = inputRGB
    while generationCount > 0:
        newPopulationToAdd = []
        selectionNumCount = selectionNum
        while selectionNumCount > 0:
            selectBin = selection(populationList)
            selectBin = selectBin[1]
            newPopulationToAdd.append(selectBin)
            selectionNumCount -= 1
        mutationNumCount = mutationNum
        while mutationNumCount > 0:
            mutatBin = mutation(populationList)
            newPopulationToAdd.append(mutatBin)
            mutationNumCount -= 1
        while newChromosome > 0:
            newChrom = newBlood()
            newPopulationToAdd.append(newChrom)
            newChromosome -= 1
        crossoverPairsCount = crossoverPairs
        while crossoverPairsCount > 0:
            crossBin = crossover(populationList)
            newPopulationToAdd.append(crossBin[0])
            newPopulationToAdd.append(crossBin[1])
            crossoverPairsCount -= 2
        newPopulationToAdd = fitnessEquation(goalRGB, newPopulationToAdd)
        for element in newPopulationToAdd:
            populationList.append(element)
        newPopulationToAdd[:] = []
        populationList.sort()
        populationList = populationList[:75]
        generationCount -= 1
        count += 1
        bestSoFar = populationList[0]
        print "After generation", (count), "the best fit chromosome is", bestSoFar[1]        
    return populationList, populationList[0], len(populationList), len(newPopulationToAdd), newPopulationToAdd
       
 
def main():
    inputBitString = raw_input("Enter the target bit string: ")
    if len(inputBitString) != 24:
        print "The input was not long enough, make sure it is 24 in length."
        main()
    else:
        pass
    for ch in inputBitString:
        if ch == '1':
            pass
        elif ch == '0':
            pass
        else:
            print "Improper values were used, please use only 1's and 0's."
            main()
    chromosomeNum = input("How many chromosomes per population?: ")
    selectionNum = input("How many chromosomes undergo selection?: ")
    mutationNum = input("How many chromosomes undergo mutation?: ")
    newChromosome = input("How many new chromosomes per generation?: ")
    crossoverPairs = input("How many crossover pairs?: ")
    if chromosomeNum == (selectionNum + mutationNum + (crossoverPairs*2)):
        pass
    else:
        print "Input numbers for chromosomes did not add up correctly, please try again.\n"
        main()
    generationCount = input("How many generations?: ")
    inputBitString = createRGB(inputBitString)
    population = createPopulation(chromosomeNum)
    populationList = fitnessEquation(inputBitString, population)
    count = 0
    gen = generation(inputBitString, populationList, chromosomeNum, selectionNum, mutationNum, newChromosome, crossoverPairs, generationCount)
    bestMatch = gen[1]
    print "The best chromosome match after the search was ", bestMatch[1], "with a fitness score of ", bestMatch[0]

main()
    
