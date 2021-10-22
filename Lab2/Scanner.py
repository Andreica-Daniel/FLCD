class Scanner:
    def __init__(self, exercise):
        self.problem = exercise
        self.line = []

    def __iter__(self):
        return self

    def detectNextToken(self):
        while not len(self.line):
            self.line = self.problem.readline()
            if not self.line:
                return 0
            self.line = self.line.split()
        return self.line.pop(0)

    def checkIfIdentifier(self, token):
        return token[0].isalpha() #???

    def checkIfConstant(self, token):
        return

    def checkIfReservedWord(self,token):
        return token in ['str','elif','else', 'if', 'int', 'bool', 'while', 'print', 'input', 'for', 'and', 'or', 'in', 'not']

    def checkIfSepartor(self,token):
        return token in ['{', '}', '[', ']', '(', ')']

    def checkIfOperator(self,token):
        return token in ['+', '-', '/', '*', '%', '==', '!=', '<', '>', '<=', '>=']

    def classifyToken(self, currentToken):
        if self.checkIfSepartor(currentToken):
            return 0
        if self.checkIfOperator(currentToken):
            return 1
        if self.checkIfReservedWord(currentToken):
            return 2
        if self.checkIfConstant(currentToken):
            return 3
        if self.checkIfIdentifier(currentToken):
            return 4
        return 5 #lexical error

    def codifyToken(self):
        return