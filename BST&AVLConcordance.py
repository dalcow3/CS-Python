from avl import *
from bst import BST
import os
from time import clock

"""
File: cs1520pgmProj5.py
Author: Chris Bruns
Description: Programming project that creates two concordances using different
classes. The first is using a BST based dictionary and the second is using an AVL
based dictionary. Each creates a text file of the built concordance and the times
of each are also recorded in the file as well as being displayed on the python
shell. In addition the user is given the option to also input a stop words file.
"""

class Entry(object):
    """A key/value pair."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def getValue(self):
        """Returns the value associated with a key"""
        return self.value

    def getKey(self):
        """Returns the key"""
        return self.key

    def setValue(self, newVal):
        """Sets the value for a key to a new value"""
        self.value = newVal

    def __eq__(self, other):
        """Equal"""
        if not isinstance(other, Entry):
            return False
        else:
            return self.key == other.key

    def __lt__(self, other):
        """Less than"""
        return self.key < other.key

    def __gt__(self, other):
        """Greater than"""
        return self.key > other.key

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    
class BSTDict(BST):
    def __init__(self):
        self._table = BST()

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        entry = Entry(key, None)
        result = self._table.find(entry)
        if result == None:
            return None
        else:
            return result.getValue()


    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        entry = Entry(key, value)
        result = self._table.find(entry)
        if result == None:
            self._table.add(entry)
        else:
            result.setValue(value)

    def __contains__(self, key):
        """Returns True if key in BSTDict otherwise returns False."""
        entry = Entry(key, None)
        result = self._table.find(entry)
        if result == None:
            return False
        else:
            return True

    def __len__(self):
        """Returns the length of the BST Dictionary"""
        return len(self._table)

    def __iter__(self):
        """Iterates through the key/values in the BST"""
        return iter(self._table)
        

    def __str__(self): 
        """Returns unordered string of the dictionary and associated values in tree format."""
        return str(self._table)


class AVLDict(AVL):
    """An AVL-based implementation of a dictionary."""
    def __init__(self):
        self._table = AVL()


    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        entry = Entry(key, None)
        result = self._table.find(entry)
        if result == None:
            return None
        else:
            return result.getValue()


    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        entry = Entry(key, value)
        result = self._table.find(entry)
        if result == None:
            self._table.add(entry)
        else:
            result.setValue(value)

    def __contains__(self, key):
        """Returns True if key in AVLDict otherwise returns False."""
        entry = Entry(key, None)
        result = self._table.find(entry)
        if result == None:
            return False
        else:
            return True

    def __len__(self):
        """Returns the length of the AVL Dictionary"""
        return len(self._table)

    def __iter__(self):
        """Iterates through the key/value pairs in the dictionary"""
        return iter(self._table)
        

    def __str__(self): 
        """Returns string of the dictionary and associated values in tree format."""
        return str(self._table)
    
def main():
    fileStopList = raw_input("Enter the name of the file of the stop list: ")
    stopDict = {} #Stop words dictionary
    if os.path.exists(fileStopList):
        stopList = open('stop_words.txt', 'r')
        for line in stopList:
            line = line.strip()
            for word in line.split():
                word = word.lower()
                stopDict[word]=word
    else:
        print "No such file existed."
        continueOn = raw_input("Do you wish to continue? y/n: ")
        if continueOn == "y":
            pass
        else:
            quit()
                               
    fileDataName = raw_input("\nEnter the name of the file to build a word concordance: ")
    if os.path.exists(fileDataName):        
        bstDict = BSTDict() #BST dictionary
        start = clock()
        fileName = open(fileDataName, 'r')
        lineCount = 0
        for line in fileName:
            line = line.strip()
            lineCount += 1
            for word in line.split():
                word = word.strip('"'+","+"."+"!"+"?"+"0"+":"+";"+"("+")"+"["+"]"+"- "+"----"+"' "+".'")
                word = word.strip("\n")
                if word != "":
                    word = word.lower()
                    if word not in stopDict:
                        if word in bstDict:
                            lineList = bstDict[word]
                            lineList.append(lineCount)
                        else:
                            bstDict[word] = [lineCount]    

        concordanceBST = open('BST Concordance', 'w') #BST File Creating
        print "\n\nBST Concordance file was created titled 'BST Concordance'"
        concordanceBST.write("Word Concordance for a BST Dictionary\n\n" \
                             "Number of words = "+str(len(bstDict._table))+"\n\n"\
                             "Word followed by the line numbers it appears in.\n\n\n")
        for word in bstDict._table:
            concordanceBST.write(str(word)+"\n\n")
        end = clock()
        runTime = end - start
        concordanceBST.write("Running time for the BST Concordance "+str(runTime)+" seconds")
        concordanceBST.close()
        print "Time to create BST Concordance =", runTime, "seconds"
    else:
        raise NameError, "File doesn't exist"
    
    avlDict = AVLDict() #AVL Dictionary
    start = clock()
    fileName = open(fileDataName, 'r')
    lineCount = 0
    for line in fileName:
        line = line.strip()
        lineCount += 1
        for word in line.split():
            word = word.strip('"'+","+"."+"!"+"?"+"0"+":"+";"+"("+")"+"["+"]"+"- "+"----"+"' "+".'")
            word = word.strip("\n")
            if word != "":
                word = word.lower()
                if word not in stopDict:
                    if word in avlDict:
                        lineList = avlDict[word]
                        lineList.append(lineCount)
                    else:
                        avlDict[word] = [lineCount]

    concordanceAVL = open("AVL Concordance", 'w') #AVL File Creating
    print "\n\nAVL Concordance file was created titled 'AVL Concordance'"
    concordanceAVL.write("Word Concordance for an AVL Dictionary\n\nNumber of " \
                         "words = "+str(len(avlDict._table))+"\n\nWord followed by the line numbers it appears in.\n\n\n")
    
    for word in avlDict._table.inorder():
        concordanceAVL.write(str(word)+"\n\n")
    end = clock()
    runTime = end - start
    concordanceAVL.write("Running time for the BST Concordance "+str(runTime)+" seconds")
    concordanceAVL.close()

    print "Time to create BST Concordance =", runTime, "seconds"


main()
