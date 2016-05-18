"""
File:
Author:
Description:
"""
from dictionary import *
import os
from avl import *
from time import clock
from hashtable import *

class HashEntry(Entry):

    def __init__(self, key, value, next):
        Entry.__init__(self, key, value)
        self.next = next
        


class HashTableDict(HashTable):
    def __init__(self):
        self._table = HashTable()

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        entry = HashEntry(key, None, next)
        result = self._table.search(entry)
        if result == None:
            return None
        else:
            return result


    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        if not key in self:
            entry = HashEntry(key, value, next)
            self._table.insert(entry)
        else:
            self._table.search(entry)
            self._table[key] = [value]

    def __contains__(self, key):
        """Returns True if key in Hash Table Dict otherwise returns False."""
        entry = HashEntry(key, None, next)
        result = self._table.search(entry)
        if result == None:
            return False
        else:
            return True

    def __len__(self):
        """Returns the length of the Hash Table Dictionary"""
        return len(self._table)

    def __iter__(self):
        """Iterates through the key/values in the Hash Table"""
        for entryItem in self._table:
            yield entryItem.getKey()
        raise StopIteration
         

    def __str__(self): 
        """Returns unordered string of the dictionary."""
        return str(self._table)

class BSTHashTable(HashDict):
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


class AVLHashTable(HashDict):
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
            
###Hash Dictionary 1)
    fileDataName = raw_input("\nEnter the name of the file to build a word concordance: ")
    if os.path.exists(fileDataName):        
        hDict = HashDict(6000) 
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
                        if word in hDict:
                            lineList = hDict[word]
                            lineList.append(lineCount)
                        else:
                            hDict[word] = [lineCount]
        concordancehDict = open("Hash Dictionary Concordance", 'w')
        print "\n\nHash Dictionary Concordance file was created titled 'Hash Dictionary Concordance'"
        concordancehDict.write("Word Concordance for a Hash Dictionary\n\n" \
                               "Number of words = "+str(len(hDict._table))+"\n\n" \
                               "Word followed by the the line numbers it appears in.\n\n\n")
        for word in hDict._table:
            if word != None:
                concordancehDict.write(str(word)+"\n\n")
        end = clock()
        runTime = end - start

        print "Time to create Hash Dictionary =", runTime, "seconds"
    else:
       raise NameError, "File doesn't exist" 

###Hash Table open-address 2)
    hTableDict = HashTableDict()
    start = clock()
    fileName = open('hw5data.txt', 'r')
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
                    if word in hTableDict:
                        lineList = hTableDict[word]
                    else:
                        hTableDict[word] = [lineCount]
    concordanceHashTableDict = open("Hash Table Dictionary Concordance", 'w')
    print "\n\nHash Table Dictionary Concordance file was created titled 'Hash Table Dictionary Concordance'"
    concordanceHashTableDict.write("Word Concordance for a Hash Table Dictionary\n\n" \
                           "Number of words = "+str(len(hTableDict._table))+"\n\n" \
                           "Word followed by the the line numbers it appears in.\n\n\n")
    for word in hTableDict._table:
        if word != None:
            concordanceHashTableDict.write(str(word)+"\n\n")
    end = clock()
    runTime = end - start
    print "Time to create Hash Table Dictionary =", runTime, "seconds"


### BST Implementation Hash Dictionary 3)
    bstHashDict = BSTHashTable()
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
                    if word in bstHashDict:
                        lineList = bstHashDict[word]
                        lineList.append(lineCount)
                    else:
                        bstHashDict[word] = [lineCount]
    concordanceBSTHashDict = open("BST Hash Dictionary Concordance", 'w')
    print "\n\nBST Implementation of a Hash Dictionary Concordance file was created titled 'BST Hash Dictionary Concordance'"
    concordanceBSTHashDict.write("Word Concordance for a BST Implementation of a Hash Dictionary\n\n" \
                           "Number of words = "+str(len(bstHashDict._table))+"\n\n" \
                           "Word followed by the the line numbers it appears in.\n\n\n")
    for word in bstHashDict._table:
        if word != None:
            concordanceBSTHashDict.write(str(word)+"\n\n")
    end = clock()
    runTimes = end - start
    print "Time to create BST Hash Dictionary =", runTimes, "seconds"

###AVL Implementation Hash Dictionary 4)
    AVLHashDict = AVLHashTable()
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
                    if word in AVLHashDict:
                        lineList = AVLHashDict[word]
                        lineList.append(lineCount)
                    else:
                        AVLHashDict[word] = [lineCount]
    concordanceAVLHashDict = open("AVL Hash Dictionary Concordance", 'w')
    print "\n\nAVL Implementation of a Hash Dictionary Concordance file was created titled 'AVL Hash Dictionary Concordance'"
    concordanceAVLHashDict.write("Word Concordance for a AVL Implementation of a Hash Dictionary\n\n" \
                           "Number of words = "+str(len(AVLHashDict._table))+"\n\n" \
                           "Word followed by the the line numbers it appears in.\n\n\n")
    for word in AVLHashDict._table:
        if word != None:
            concordanceAVLHashDict.write(str(word)+"\n\n")
    end = clock()
    runTimes = end - start
    print "Time to create BST Hash Dictionary =", runTimes, "seconds"    
main()
