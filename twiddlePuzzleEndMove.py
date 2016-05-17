
"""
Author: Chris Bruns
File: twiddlePuzzleEndMove.py
Description: Solution to solving the Twiddle Puzzle problem using a BFS type
search. This puzzle will display the final move but the information of the
entire path is not currently available. The performance is slightly reduced
from that of the twiddlePuzzleSolve.py. 
"""

"""Main Function"""
from queue import *
from node import *
from graph import *
import time

def main():
    """The input of the string as the puzzle"""
    dictionary = {}
    twiddleInput = [[]]
    twiddleGoal = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    twiddleGoal = tuple(twiddleGoal)
    twiddleOrder = raw_input("Enter your board as a string of numbers 1-9 with no spaces: ")
    for ch in twiddleOrder:
        twiddleInput[0].append(ch)
    bfsOutput = bfs(twiddleInput, twiddleGoal)
    print "\n",bfsOutput[0], "in",  bfsOutput[1] , "seconds"
    print "There are", bfsOutput[2], "boards still in the frontier."
    print bfsOutput[3], "boards were considered before finding a solution."
    print "There was a total number of", (bfsOutput[2] + bfsOutput[3]),"boards that were created."
    print "The final move was", bfsOutput[5]
    print bfsOutput[4]



def bfs(twiddleInput, twiddleGoal):
    import time
    dictionary = {}
    start = time.clock()
    node = twiddleInput
    if node == twiddleGoal:
        return node
    frontier = LinkedQueue()
    frontier.enqueue(node)
    explored = []
    while frontier is not frontier.isEmpty():
        node = frontier.dequeue()
        explored.append(node)
        for child in possibleMoves(node):
            dictChild = child
#            dictionary[dictChild[0]] = dictChild[1:]
            if child not in explored:
                pathList = []
                dictionary[child] = [child]
                if twiddleGoal == child[0]:
                    pathList.append(child[2])
                    end = time.clock()
                    time = end - start
                    return "A solution was found", time, len(frontier), len(explored), dictionary[child], pathList
                frontier.enqueue(child)
    return None

    
"""Possible moves"""
def possibleMoves(twiddleInput):
    firstMove = [aCC(twiddleInput), twiddleInput, "aCC"]
    secondMove = [aC(twiddleInput), twiddleInput, "aC"]
    thirdMove = [bCC(twiddleInput), twiddleInput, "bCC"]
    forthMove = [bC(twiddleInput), twiddleInput, "bC"]
    fifthMove = [cCC(twiddleInput), twiddleInput, "cCC"]
    sixthMove = [cC(twiddleInput), twiddleInput, "cC"]
    seventhMove = [dCC(twiddleInput), twiddleInput, "dCC"]
    eighthMove = [dC(twiddleInput), twiddleInput, "dC"]
    return firstMove, secondMove, thirdMove, forthMove, fifthMove, sixthMove, seventhMove, eighthMove
    
def aCC(twiddleInput):
    newOrder = [1,4,2,0,3,5,6,7,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString

def aC(twiddleInput):
    newOrder = [3,0,2,4,1,5,6,7,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString) 
    return newTwiddleString

def bCC(twiddleInput):
    newOrder = [0,2,5,3,1,4,6,7,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString
    
def bC(twiddleInput):
    newOrder = [0,4,1,3,5,2,6,7,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString

def cCC(twiddleInput):
    newOrder = [0,1,2,3,5,8,6,4,7]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString

def cC(twiddleInput):
    newOrder = [0,1,2,3,7,4,6,8,5]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString

def dCC(twiddleInput):
    newOrder = [0,1,2,4,7,5,3,6,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString

def dC(twiddleInput):
    newOrder = [0,1,2,6,3,5,7,4,8]
    testTwiddleString = twiddleInput[0]
    testTwiddleString = [testTwiddleString[i] for i in newOrder]
    newTwiddleString = tuple(testTwiddleString)
    return newTwiddleString
    


main()
