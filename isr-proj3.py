#!/usr/bin/python3.4

import os
import sys
"""
File: isr-prog3
Author: Chris Bruns
Description: Program that generates a dictionary with corresponding postings list
corressponding to the files that were imported into the program. The terms go through
a permutation with each new term added to a tree structure. The user is prompted
to provide a search query that is then processed through the tree one search term
at a time. Through finding the union and intersection of different lists created
the user is then given a list of the files that match the search query.
"""

"""Function created to rotate the word provided creating all the different permutations."""
def moveCharacters(word):
    characters=list(word)
    char=characters[len(characters)-1]
    characters.pop()
    characters.insert(0, char)    
    return ''.join(characters)

"""Helper function to add the '$' symbol to each word."""
def addMoneySign(word):
    new = list(word)
    new.append("$")
    str(new)
    return new
"""Helper function to aid in the search for the permuterms taking into account
any '*' characters within the search."""
def searchHelper(tree, searchString):
    searchList = list(searchString)
    if searchList[0] == "*":
        return tree.find(searchList[1:])[0] #everything after the first item
    elif searchList[-1] == "*":
        return tree.find(searchList[:-1])[0] #returns the list except for the end value
    else:
        return tree.find(searchString)[0]

"""A helper function during the search. Used to create a union of locations
the query is found as it goes through multiple files."""
def fullUnion(first, lst):
    if len(lst) == 1:
        return first
    else:
        trial = list(set(first) | set(lst[1]))
        del(lst[0])
        return fullUnion(trial, lst)
                     
"""A helper function used during the search. After going through all of the
files used to find the intersection of final results."""
def fullIntersection(first, lst):
    if len(lst) == 1:
        return first
    else:
        trial = list(set(first) & set(lst[1]))
        del(lst[0])
        return fullIntersection(trial, lst)

   
def main():                              
    fileList =  sys.argv
    if len(fileList) == 1:
        print("Error: A list of files is required on the command line. Please try again.")
        print("Usage: ./isr-prog1 <file1> [file2] ... [fileN]")
        quit()
     for i in files:
        fileList.append(i)
    fileNum = 1
    print("Search string: ")
    searchTerms = sys.argv
    searchList = []
    for i in searchTerms:
        searchList.append(i)
    searchList = []
    terms = searchTerms.split()
    for i in terms:
        searchList.append(i)
    conDict = {}
    p = PorterStemmer()
    for i in fileList:
        if os.path.exists(i):
            continue
        else:
            print("Error: One or more of the files did not exist. Please try again.")
            print("Usage: ./isr-prog1 <file1> [file2] ... [fileN]")
            quit()
    tree = BST()
    for i in fileList: 
        appearanceList = []
        if os.path.exists(i):        
            fileName = open(i, 'r')
            output = ''
            for line in fileName:
                line = line.strip()
                for word in line.split():
                    word = word.replace("(", "")
                    word = word.replace(")", "")
                    word = word.replace("#", "")
                    word = word.replace("*", "")
                    word = word.replace("+", "")
                    word = word.replace("&", "")
                    word = word.replace("=", "")
                    word = word.replace('"', "")
                    word = word.replace("/", "")
                    word = word.replace("<", "")
                    word = word.replace(">", "")                    
                    word = word.replace("-", "")
                    word = word.replace("'", "")
                    word = word.replace(",", "")
                    word = word.replace(".", "")
                    word = word.replace("}", "")
                    word = word.replace("{", "")
                    word = word.replace("[", "")
                    word = word.replace("]", "")
                    word = word.strip('"'+","+"."+"!"+"?"+"0"+":"+";"+"("+")"+"["+"]"+"- "+"----"+"&"+"'s"+"."+"|")
                    word = word.strip("\n")
                    output = p.stem(word, 0, len(word)-1)
                    if output != "":
                        output = output.lower()
                        if output in conDict:
                            appearanceList = conDict[output]
                            if fileNum in appearanceList:
                                continue
                            else:
                                appearanceList.append(fileNum)
                        else:
                            conDict[output] = [fileNum]
                               
            fileNum += 1
            fileName.close()
            
    if len(conDict) != 0 and len(fileList) > 0:
        print("\n\nLegend:")
       # del fileList[0]
        count = 1
        for i in fileList:
            print(count," "+i)
            count+=1
        print()
    else:
        print("Error: A list of files is required on the command line or the files did not exist. Please try again.")
        print("Usage: ./isr-prog1 <file1> [file2] ... [fileN]")

    location = 0
    length = len(conDict)-1

    halfway = length//2
    newCount = 0

    start = timeit.default_timer()
            
    for i in conDict:
        counter = 0
        altWord = i
        altWord = addMoneySign(altWord)
        while counter < len(altWord):
            altWord = moveCharacters(altWord)
            tree.add([altWord, location])
            counter+=1
        location+=1
    stop = timeit.default_timer()
    print("Finished tree")
    print(stop-start)
    unionList = []
    intersectionList = []
    for i in searchList:
        termList = []
        locationList = []        
        solutions = (searchHelper(tree, str(i)))
#        for x in solutions:
#            termList.append(x)
        for x in solutions:
            loc = x[1]
            location = list(conDict.values())[loc]
 #           words = list(conDict.keys())[loc]
 #           print(words)
            locationList.append(location)
        unionList.append(fullUnion(locationList[0], locationList))
 #   print(completeList)
#    print(unionList)
#    print(locationList)
#    print(fullIntersection(unionList[0], unionList))        
    finalList = fullIntersection(unionList[0], unionList)
    finalList = sorted(finalList)
    print("Files that contain the intersection of the search terms")
    for i in finalList:
        print(fileList[i-1])

    repeat = 1
    counting = 0
    while repeat !=0:
        searchTerms = input("\nEnter the search terms you wish to look for: ")
        searchList = []
        terms = searchTerms.split()
        for i in terms:
            searchList.append(i)
        for i in searchList:
            termList = []
            locationList = []        
            solutions = (searchHelper(tree, str(i)))
            for x in solutions:
                loc = x[1]
                location = list(conDict.values())[loc]
                locationList.append(location)
            unionList.append(fullUnion(locationList[0], locationList))
        finalList = fullIntersection(unionList[0], unionList)
        finalList = sorted(finalList)
        print("Files that contain the intersection of the search terms")
        for i in finalList:
            print(fileList[i-1])
        if counting < 2:
            counting += 1
            repeat = 1
        else:
            repeat = 0
        
"""

    if len(conDict) != 0:
        maxLen = max(len(x) for x in conDict)
        listLen = len(fileList)
        print("Word"+" "*(maxLen-4)+"Posting")
        print("-"*(11+maxLen+listLen))
        for word in sorted(conDict):
            numbers = str(conDict[word])
            print(word + " "*(maxLen - (len(word)-3)) + numbers.strip('[]'))

    if len(permDict) != 0:
        maxLen = max(len(x) for x in permDict)
        listLen = len(fileList)
        print("Word"+" "*(maxLen-4)+"Posting")
        print("-"*(11+maxLen+listLen))
        for word in sorted(permDict):
            numbers = str(permDict[word])
            print(word + " "*(maxLen - (len(word)-3)) + numbers.strip('[]'))
"""


class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
class LinkedQueue(object):
    """ Link-based queue implementation."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        newNode = Node (newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode  
        self._size += 1

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._front.data

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result


class EmptyTree(object):
    """Represents an empty tree."""

    # Supported methods

    def isEmpty(self):
        return True

    def __str__(self):
        return ""

    def __iter__(self):
        """Iterator for the tree."""
        return iter([])

    def preorder(self, lyst):
        return

    def inorder(self, lyst):
        return

    def postorder(self, lyst):
        return

    # Methods not supported but in the interface for all
    # binary trees

    def getRoot(self):
        raise AttributeError ("Empty tree")

    def getLeft(self):
        raise AttributeError ("Empty tree")
    
    def getRight(self):
        raise AttributeError ("Empty tree")

    def setRoot(self, item):
        raise AttributeError ("Empty tree")

    def setLeft(self, tree):
        raise AttributeError ("Empty tree")
    
    def setRight(self, tree):
        raise AttributeError ("Empty tree")

    def removeLeft(self):
        raise AttributeError ("Empty tree")
    
    def removeRight(self):
        raise AttributeError ("Empty tree")

class BinaryTree(object):
    """Represents a nonempty binary tree."""

    # Singleton for all empty tree objects
    THE_EMPTY_TREE = EmptyTree()

    def __init__(self, item):
        """Creates a tree with
        the given item at the root."""
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE

    def isEmpty(self):
        return False

    def getRoot(self):
        return self._root

    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right

    def setRoot(self, item):
        self._root = item

    def setLeft(self, tree):
        self._left = tree
    
    def setRight(self, tree):
        self._right = tree

    def removeLeft(self):
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left
    
    def removeRight(self):
        right = self._right
        self._right = BinaryTree.THE_EMPTY_TREE
        return right

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "| " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result
        return strHelper(self, 0)




class BST(object):

    def __init__(self):
        self._tree = BinaryTree.THE_EMPTY_TREE
        self._size = 0


    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._tree)

    def __iter__(self):
        return iter(self.inorder())

    def find(self, target):
        """Returns data if target is found or None otherwise."""
        goals = []
        def findHelper(tree):
            if tree.isEmpty():
                return None
            value = tree.getRoot()
            value = list(value[0])
            targetItem = list(target)
            if len(value) == len(targetItem):
                if targetItem == value:
                    goals.append(tree.getRoot())
                    return goals
                elif targetItem < value:
                    return findHelper(tree.getLeft())
                else:
                    return findHelper(tree.getRight())
            elif len(targetItem) < len(value):
                newValue = value[:len(targetItem)]
                if targetItem == newValue:
                    goals.append(tree.getRoot())
                    return findHelper(tree.getLeft()), findHelper(tree.getRight())
                elif targetItem < newValue:
                    return findHelper(tree.getLeft())
                else:
                    return findHelper(tree.getRight())
                
            else:
                if targetItem < value:
                    return findHelper(tree.getLeft())
                else:
                    return findHelper(tree.getRight())
        return goals, findHelper(self._tree)

    def add(self, newItem):
        """Adds newItem to the tree."""

        # Helper function to search for item's position 
        def addHelper(tree):
            currentItem = tree.getRoot()
            left = tree.getLeft()
            right = tree.getRight()
            
            # New item is less, go left until spot is found
            if newItem < currentItem:
                if left.isEmpty():
                    tree.setLeft(BinaryTree(newItem))
                else:
                    addHelper(left)                    

            # New item is greater or equal, 
            # go right until spot is found
            elif right.isEmpty():
                tree.setRight(BinaryTree(newItem))
            else:
                addHelper(right)
            # End of addHelper

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTree(newItem)

        # Otherwise, search for the item's spot
        else:
            addHelper(self._tree)
        self._size += 1



main()




