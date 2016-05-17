"""
File: cs1520pgmProj4.py
Author: Christopher Bruns
Description: A GUI program that allows a user to input a file name to be used or
created. The file is then turned into a list in which the user is able to determine
the number of lines, view, edit, replace, delete, or insert new lines into the file.
"""



from Tkinter import *
import os, sys, tkMessageBox
from myPositionalList import LinkedPositionalList

class Application(Frame):
    def __init__(self, fileOpen, master=None):
        Frame.__init__(self,master)
        self.master.title("Text-Editor Program")
        self.master.geometry("600x600")
        self.grid()
        self._createWidgets()
        if os.path.exists(fileOpen):
            f=open(fileOpen, 'r')
            self._listTest = []
            for line in f:
                line = line.strip('\r'+"\n"+" ")
                self._listTest.append(line)
            self._newList = LinkedPositionalList()
            for i in self._listTest:
                self._newList.insert(i)
        else:
            f=open(fileOpen, 'w')
            self._listTest = []
            reverseList = self._listTest[::-1]
            self._newList = LinkedPositionalList()
            


    def _createWidgets(self):
        """Creating the GUI and placing the objects and buttons on the screen
            in an organized fashion."""

        """Number of Lines"""
        self._linePane = Frame(self)
        self._linePane.grid()
        numberOfLines = Button(self._linePane,
                               text="Number of Lines",
                               command=self._numLines)
        numberOfLines.grid(row=0, column=0, sticky=W)
        self._numLinesString = StringVar()
        numLinesEntry = Entry(self._linePane, justify="center", width = 8,
                         textvariable=self._numLinesString)
        numLinesEntry.grid(row=0, column=1)

        """Current Line"""
        self._currentPane=Frame(self)
        self._currentPane.grid(row=2, column=0)
        currentLineButton = Button(self._currentPane,
                                   text='Show Current Line',
                                       command=self._currentLine)
        currentLineButton.grid(row=0, column=0, sticky=W)
        self._currentLineString = StringVar()
        currentLineEntry = Entry(self._currentPane,
                                 textvariable = self._currentLineString)
        currentLineEntry.grid(row=0, column = 1, sticky=E+W, ipadx=125)

        """Viewing File Lines Buttons"""
        self._buttonPane = Frame(self)
        self._buttonPane.grid(row=6, column=0, columnspan=4)
        
        firstLineButton = Button(self._buttonPane,
                              text='Show First Line',
                                 command=self._firstLine)
        firstLineButton.grid(row=1, column=0, sticky=W)
        nextLineButton = Button(self._buttonPane,
                                text='Show Next Line',
                                    command=self._nextLine)
        nextLineButton.grid(row=2, column=0, sticky=W)
        previousLineButton = Button(self._buttonPane,
                                text='Show Previous Line',
                                    command=self._previousLine)
        previousLineButton.grid(row=3, column=0, sticky=W)
        lastLineButton = Button(self._buttonPane,
                                text='Show Last Line',
                                    command=self._lastLine)
        lastLineButton.grid(row=4, column=0, sticky=W)


    
        """Buttons to insert, delete, or replace current line"""
        self._lineEditPane = Frame(self)
        self._lineEditPane.grid(row=5, column=0)

        insertButton = Button(self._lineEditPane,
                              text="Insert Line",
                              command=self._newLine)
        insertButton.grid(row=0, column=0)
        replaceButton = Button(self._lineEditPane,
                               text='Replace Line',
                               command=self._replaceLine)
        replaceButton.grid(row=0, column=1)
        deleteButton = Button(self._lineEditPane,
                              text='Delete Line',
                              command=self._deleteLine)
        deleteButton.grid(row=0, column=2)
        
        
        """Entry Boxes to Display Lines from File"""
        self._firstLineString = StringVar()
        firstLineEntry = Entry(self._buttonPane,
                               textvariable = self._firstLineString)
        firstLineEntry.grid(row=1, column=1, ipadx=125)
        self._nextLineString = StringVar()
        nextLineEntry = Entry(self._buttonPane,
                               textvariable = self._nextLineString)
        nextLineEntry.grid(row=2, column=1, ipadx=125)
        self._previousLineString = StringVar()
        previousLineEntry = Entry(self._buttonPane,
                               textvariable = self._previousLineString)
        previousLineEntry.grid(row=3, column=1, ipadx=125)
        self._lastLineString = StringVar()
        lastLineEntry = Entry(self._buttonPane,
                               textvariable = self._lastLineString)
        lastLineEntry.grid(row=4, column=1, ipadx=125)

        
        """Entry Boxes to Type new Lines"""
        typePrompt = Label(self,
                           text="Type a new line here")
        typePrompt.grid(row=3)
        self._newTextLine = StringVar()
        newLineEntry = Entry(self,
                             textvariable = self._newTextLine)
        newLineEntry.grid(row=4, sticky=W+E)


    def _numLines(self):
        """Determines the number of lines currently in the file."""
        num=len(self._listTest)
        self._numLinesString.set(num)

    def _newLine(self):
        """Inserts a new line at the point in front of the cursor."""
        line=self._newTextLine.get()
        self._newList.insert(line)
        self._listTest.append(line)

    def _replaceLine(self):
        """Replace the current line with the line typed into the entry box."""
        line=self._newTextLine.get()
        self._newList.replace(line)

    def _deleteLine(self):
        """Deletes the current line from the file."""
        current=self._currentLine()
        self._newList.remove()
        self._listTest.pop()

    def _currentLine(self):
        """Displays the current line that the cursor is on."""
        if self._newList.isEmpty():
            text= "No current line to show"
            self._currentLineString.set(text)
        else:
            self._newList.first()
            text=self._newList.next()
            self._currentLineString.set(text)
            self._newList.previous()
        
    def _firstLine(self):
        """Displays the first line in the file"""
        moveCursor= self._newList.first()
        text=self._newList.next()
        self._firstLineString.set(text)

    def _nextLine(self):
        """Moves the cursor to the next line and prints that line in the entry box.
            If no next line is available it prints that in the box."""
        if self._newList.hasNext():
            text=self._newList.next()
            self._nextLineString.set(text)
        else:
            text="No next line available"
            self._nextLineString.set(text)

    def _previousLine(self):
        """Moves the curosr to the previous line and prints the line in the entry box.
            If no previous line is present that is displayed in the box."""
        if self._newList.hasPrevious():
            previous=self._newList.previous()
            self._previousLineString.set(previous)
        else:
            previous="No previous line avaiable"
            self._previousLineString.set(previous)

    def _lastLine(self):
        """Displays the last line of the file in the entry box."""
        moveCursor=self._newList.last()
        text=self._newList.previous()
        self._lastLineString.set(text)

def main():
    """Instantiate and pop up the window."""
    print "The program will ask you to input the name of the file you wish to load. \nIt will then open a screen for you to execute the commands and actions you \nwish to perform on the file.\n\n"
    fileOpen = raw_input("Enter the name of the file you wish to open or create: ")
    Application(fileOpen).mainloop()

main()

