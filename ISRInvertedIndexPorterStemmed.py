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
     for i in files:
        fileList.append(i)
    fileNum = 1
    conDict = {}
    p = PorterStemmer()
    for i in fileList:
        appearanceList = []
        if os.path.exists(i):        
            fileName = open(i, 'r')
            output = ''
            for line in fileName:
                line = line.strip()
                for word in line.split():
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

    if len(conDict) != 0:
        maxLen = max(len(x) for x in conDict)
        listLen = len(fileList)
        print("Word"+" "*(maxLen-4)+"Posting")
        print("-"*(11+maxLen+listLen))
        for word in sorted(conDict):
            numbers = str(conDict[word])
            print(word + " "*(maxLen - (len(word)-3)) + numbers.strip('[]'))

main()



