"""
File: cs1520pgmProj2.py
Author: Chris Bruns
Description: Program to input a maze from a .txt file, change the maze into
a grid, and then use a stack to attempt to find a path through the maze.
"""

from grid import Grid
from stack import ArrayStack

def main():
    maze = openMaze()
    print maze
    (startRow, startColumn) = startPos(maze)
    (endRow, endColumn) = endPos(maze)
    print "Starting point: " + str((startRow, startColumn)) + "\nEnding point: " + str((endRow, endColumn))
    solved = solveMaze(startRow, startColumn, maze)
    if solved != None:
        print "Success!"
        print maze
    if solved == None:
        print "Maze Failed!"


def openMaze():
    fileName = raw_input("Enter the name of the maze you wish to test: ")
    fileMaze = open(fileName, 'r')
    rows = fileMaze.readline()
    rows = int(rows)
    columns = fileMaze.readline()
    columns = int(columns)
    maze = Grid(rows, columns, '*')
    for row in xrange(rows):
        line = fileMaze.readline().strip()
        column = 0
        for character in line:
            maze[row][column] = character
            column += 1
    return maze

def startPos(maze):
    for row in xrange(maze.getHeight()):
        for column in xrange(maze.getWidth()):
            if maze[row][column] == 'P':
                return [row, column]

def endPos(maze):
    for row in xrange(maze.getHeight()):
        for column in xrange(maze.getWidth()):
            if maze[row][column] == 'T':
                return [row, column]

def solveMaze(row, column, maze):
    stack = ArrayStack()
    stack.push((row, column))

    while not stack.isEmpty():
        (row, column) = stack.peek()
        if maze[row][column] == 'T':
            return stack
        elif maze[row][column] != '.':
            maze[row][column] = '.'
            counter = 0  ###adjacent cells based on changing x,y values so need 4 options
            if row != 0 and not maze[row - 1][column] in ('*', '.'):
                stack.push((row-1, column))
                counter += 1
            if row + 1 != maze.getHeight() and not maze[row + 1][column] in ('*', '.'):
                stack.push((row + 1, column))
                counter += 1
            if column + 1 != maze.getWidth() and not maze[row][column + 1] in ('*', '.'):
                stack.push((row, column + 1))
                counter += 1
            if column != 0 and not maze[row][column -1] in ('*', '.'):
                stack.push((row, column - 1))
                counter += 1
        if counter == 0:
            stack.pop()
    return None

main()
