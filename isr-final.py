#!/usr/bin/python3.4


from os import listdir
from os.path import isfile, join
from os import walk
import os
import sys
import math

#direc = input("enter directory ")
#os.chdir(direc)

def main():
    directories = input("Enter the directories ")
    ###Items in the directory
    directoryList = []
 #   print(directories)
    for i in directories.split(" "):
        directoryList.append(i)
    tester = []
    print(directoryList)
    ###List containing name of the category, number of words, and the term dictionary. 
    categoryNameAndList = []
#    for i in os.listdir(os.getcwd()):
#        directoryList.append(i)
 #       print(i)
    for i in directoryList:
        try:
            os.chdir(i)
            names = []
            catName = str(i)
            fileNames = []
 #           print(os.getcwd())
            categoryTerms = []
            count = 0
            for x in os.listdir(os.getcwd()):
                if isfile(x):
                    if x == '.DS_Store':
                        pass
                    else:
                        count += 1
                        file = str(x)
                        fileListOfWords = readingFile(file)
                        for y in fileListOfWords:
                            categoryTerms.append(y)
            os.chdir("..")
 #           print(os.getcwd())
            
            newDict = {}
            termDict = dictionaryUpdate(newDict, categoryTerms)
            nameSizeDict = [i, len(categoryTerms), termDict, count]
            categoryNameAndList.append(nameSizeDict)
        except:
            pass
        """
            try:
                if isfile(i):
                    file = str(i)
                    fileListOfWords = readingFile(file)
                    for y in fileListOfWords:
                        tester.append(y)
                newDict= {}
                termDict = dictionaryUpdate(newDict, categoryTerms)
                nameSizeDict = [i, len(categoryTerms), termDict]
                categoryNameAndList.append(nameSizeDict)
                alt = [str(os.getcwd()), len(categoryTerms), termDict]
                categoryNameAndList.append(alt)
            except:
                pass

                """
#    termDict = {}
#    newDict = dictionaryUpdate(termDict, tester)
#    nameSizeDict = [str(i), len(tester), newDict]
 #   categoryNameAndList.append(nameSizeDict)   
    first = categoryNameAndList[0]
#    print(len(categoryNameAndList))
    for first in categoryNameAndList:
        print("Category name is " + first[0])
        print("Total number of words is " + str(first[1]))
        print("Number of different terms is " + str(len(first[2])))
        print("Number of files is " + str(first[3])+"\n")

    fileToSort = input("Enter the file you wish to categorize: ")
    fileToSortList = readingFile(fileToSort)
    fileToSortDict = {}
    fileToSortDict = dictionaryUpdate(fileToSortDict, fileToSortList)
    for i in fileToSortDict:
        print(i)
 #   print(fileToSortDict)
def logCategory(fileDictionary, allCategories):
    return None
    

#song = input("Enter the song text file: ")
def readingFile(fileName):
    textFile = open(fileName, 'r')
    wordList = []
    for line in textFile:
        line = line.strip()
        for word in line.split():
            word = word.lower()
            word = word.replace('"', "")
            word = word.replace(".", "")
            word = word.replace("?", "")
            word = word.replace(",", "")
            if "'" in word:
                if word[word.index("'")+1:] == 's':
                    wordList.append(word[:word.index("'")])
                    wordList.append("is")
                elif word[word.index("'")+1:] == 'm':
                    wordList.append("i")
                    wordList.append("am")
                elif word[word.index("'")+1:] == 're':
                    wordList.append(word[:word.index("'")])
                    wordList.append("are")
                elif word[word.index("'")+1:] == 've':
                    wordList.append(word[:word.index("'")])
                    wordList.append("have")                
                elif word[word.index("'")+1:] == 'clock':
                    wordList.append(word[word.index("'")+1:])
                    wordList.append("of")
                    wordList.append("the")
                elif word[word.index("'")+1:] == 'd':
                    wordList.append("did")
                    wordList.append(word[word.index("'")+1:])                
                elif word[word.index("'")+1:] == 'cause':
                    wordList.append("because")
                elif word[word.index("'")+1:] == '':
                    wordList.append(word[:word.index("'")])
                elif word[word.index("'")+1:] == 'tch':
                    wordList.append("can")
                    wordList.append("you")
                    wordList.append("not")
                elif word[word.index("'")+1:] == 't':
                    if word[:word.index("'"):] == 'wouldn':
                        wordList.append("would")
                        wordList.append("not")
                    elif word[:word.index("'"):] == 'ain' or 'isn':
                        wordList.append("is")
                        wordList.append("not")
                    elif word[:word.index("'"):] == 'don':
                        wordList.append("do")
                        wordList.append("not")
                    elif word[:word.index("'"):] == 'can':
                        wordList.append("can")
                        wordList.append("not")
                    else:
                        wordList.append(word)
                else:
                    wordList.append(word)
            else:
                wordList.append(word)
                continue

    textFile.close()
    return wordList
#first = (readingFile("PianoMan"))

songDictionary = {}
def dictionaryUpdate(dictionary, fileList):
    for i in fileList:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary
#print(dictionaryUpdate(songDictionary, first))

#tally = (song + " Final Tally")
#word = "wouldn't"
#print(word[:word.index("'")])
#with open((song+" Final Tally"), 'w') as file:
#    file.write("Billy Joel: Piano Man\n")
#    for word in sorted(songDictionary):
#        count = songDictionary[word]
#        file.write(word + ": " + str(count) + "\n")
#    file.write("Total is: " + str(len(wordList)))

#file.close()
      
main()   

        

