#!/usr/bin/python3.4

import os
import sys
"""
File: isr-prog1
Author: Chris Bruns
Description: Program that generates a dictionary with corresponding postings li$
corressponding to the files that were imported into the program. The files are
listed at the beginning of the output. After each word in the output will be
the numbers from the legend identifying which of the files contain the word. 
"""
   
def main():
                              
    fileList =  sys.argv
    if len(fileList) == 1:
        print("Error: A list of files is required on the command line. Please try again.")
        print("Usage: ./isr-prog1 <file1> [file2] ... [fileN]")
        quit()
    else:
        print("\n\nLegend:")
        del fileList[0]
        count = 1
        for i in fileList:
            print(count," "+i)
            count+=1
        print()
        fileNum = 1
        conDict = {} ###creating the dictionary to store the words as keys and the values attached to each key are lists
        for i in fileList: ###containing the number of the files from the legend that contain the word
            appList = []
            if os.path.exists(i):        
                fileName = open(i, 'r')
                for line in fileName:
                    line = line.strip()
                    for word in line.split():
                        if word != "":
                            if word in conDict:
                                appList = conDict[word]
                                if fileNum in appList:
                                    continue
                                else:
                                    appList.append(fileNum)
                            else:
                                conDict[word] = [fileNum]
                fileNum += 1
            else:
                raise print ("File doesn't exist") ###raises an error if one of the given files doesn't exist
    ###printing the postings list and formating 
        print("Word"+(" ")*45+("Posting"))
        print("-"*70)
        for word in sorted(conDict):
            numbers = str(conDict[word]) 
            print('{0:28s} {1:50s}'.format(word, numbers.strip('[]')))

        p = PorterStemmer()
        output = ''
        for word in sorted(conDict):
            output += p.stem(word, 0, len(word)-1)
            word = ''
        print (output,"\n")
            

main()


