"""
Author: Chris Bruns
Title: HW3.py
Description:
"""
import itertools

def possibleMoves(boardList, changeItems, goalState):
    """
    Takes in the original input board. The possible moves (changeItems) is iterated
    through and all possible combinations are created. This is then used to compare
    to the indexes in the current board to determine if a move is legal or not. And the
    goal state is currently not being used yet... It returns a dictionary with the
    key the being the new board and the value being how it was altered.
    """
    newList = []
    characterList = []
    combinations = []
    movesList = []
    testDict = {}
    for i, j in enumerate(boardList):
        if j == '*':
            characterList.append(i)
    r = 3
    while r > 0:
        for combination in changeItems:
            for p in itertools.combinations(combination, r):
                combinations.append(p)
                combinationVariance = p
                testForSimilar = set(characterList) & set(combinationVariance)
                if len(testForSimilar) == 0:
                    for part in boardList:
                        newList.append(part)
                    for num in combinationVariance:
                        newList[num] = '*'
                    newList = ''.join(newList)
                    testDict[newList] = combinationVariance
                    newList = []
        r -= 1
    return testDict


def validMoves():
    """
    Possible moves allowed in the game returned as a list
    """
    movesList = []
    row1 = [0,1,2]
    row2 = [3,4,5]
    row3 = [6,7,8]
    column1 = [0,3,6]
    column2 = [1,4,7]
    column3 = [2,5,8]
    movesList.append(row1)
    movesList.append(row2)
    movesList.append(row3)
    movesList.append(column1)
    movesList.append(column2)
    movesList.append(column3)
    return movesList


def miniMax(key, moves, goalState):
    """
    Recursively goes through the keys and attaches a count value used to deterimine if
    good for max or min in the main function.
    """
    count = 9
    while key != goalState:
        keys = possibleMoves(key, moves, goalState)
        newKeys = keys.keys()
        newValues = keys.values()
        key = newKeys[0]
        if key == goalState:
            if count % 2 == 0:
                positionCount = count
            else:
                positionCount = -10
        value = newValues[0]
        count -= 1
    return [key, value, positionCount]

    
def main():
    board = raw_input("Enter the starting state for the board (- or *): ")
    if len(board) != 9:
        print "The input was not long enough, make sure it is 9 characters."
        main()
    else:
        pass
    for ch in board:
        if ch == '*':
            pass
        elif ch == '-':
            pass
        else:
            print "Improper values were used, please construct the board of only '-' and '*'."
            main()
    boardList = []
    for ch in board:
        boardList.append(ch)
    newBoard = ''.join(boardList)
    goalState = ['*','*','*','*','*','*','*','*','*']
    goalState = ''.join(goalState)
    moves = validMoves()
    changes = possibleMoves(newBoard, moves, goalState)
    changesDict = changes
    keys = changesDict.keys()
    possibilities = []
    for key in keys:
        if key != goalState:
            add = miniMax(key, moves, goalState)
            possibilities.append(add)        
        else:
            add = [goalState, changesDict[key], 10]
            possibilities.append(add)
    maxMoves = []
    minMoves = []
    for element in possibilities:
        if element[2] > 0:
            maxMoves.append(element)
        else:
            minMoves.append(element)
    maxBestMarkers = []
    minBestMarkers = []
    if len(maxMoves) != 0:
        maxBest = maxMoves.pop()
        maxBest = maxBest[1]
        for num in maxBest:
            maxBestMarkers.append(num+1)
    if len(minMoves) != 0:
        minBest = minMoves.pop()
        minBest = minBest[1]
        for num in minBest:
            minBestMarkers.append(num+1)
    solution = []
    if len(maxBestMarkers) != 0:
        solution = maxBestMarkers
        solution.append("and you will eventually win.")
    else:
        solution = minBestMarkers
        solution.append("and you will eventually lose.")        
    print "Your best option is to place marker(s) at position(s)", str(solution)[1:-1]

main()
