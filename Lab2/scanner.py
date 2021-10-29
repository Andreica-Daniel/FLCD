from Lab2.symbolTable import SymbolTable, Pair
import re

class Scanner:
    def __init__(self, excercise):
        self.exercise = excercise
        self.symbolTable = SymbolTable()
        self.line = []
        self.lineNumber = 0
        self.tokenNumber = 0
        self.prevToken = 0
        self.pif = []

    def __iter__(self):
        return self

    def addToPIF(self, classification, token, index):
        pair = Pair(token, index)
        self.pif.append([classification, pair])

    def getPIF(self):
        return self.pif

    #returns the next token
    def nextToken(self):
        while not len(self.line):
            self.line = self.exercise.readline()
            if not self.line:
                return 0
            self.line = self.line.split()
            self.lineNumber += 1
            self.tokenNumber = 0
        self.tokenNumber += 1
        currentToken = self.line.pop(0)
        return currentToken

    def codifyToken(self, currentToken):
        #check if token exists in token.in
        with open("token.in") as f:
            for line in f:
                newLine = line.split()
                if currentToken == newLine[0]:
                    return int(newLine[1])

        #check if it isidentifier
        if re.match("^([a-zA-Z_$][a-zA-Z\\d_$]*)$", currentToken):
            self.symbolTable.addElement(currentToken)
            return 1

        #check if it is constant
        if currentToken.isdigit():
            self.symbolTable.addElement(currentToken)
            return 2
        return -1

    def classifyCodification(self, code):
        if code == 1:
            return 'identifier'
        if code == 2:
            return 'constant'
        if 3 <= code <= 16:
            return 'reserved-word'
        if 17 <= code <= 27:
            return 'operator'
        if 28 <= code <= 35:
            return 'separator'
        return 'lexical error'