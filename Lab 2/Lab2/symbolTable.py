class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    #getters and setters for key and value
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key


class SymbolTable:
    def __init__(self):
        self.list = []

    '''
    Check if a key exists in the sorted symbol table.
    input: pair - Pair(key, value)
    return: position of the key, if it already exists
            -1, otherwise
    '''
    def checkIfElementExists(self, pair):
        for i in range(len(self.list)):
            if self.list[i].getKey() == pair.getKey():
                return self.list[i].getValue()
        return -1

    '''
    Adds a new element in the symbol table.
    input: token - the token to be added
    return: None, if that key already exist
    '''
    def addElement(self, token):
        pair = Pair(token, len(self.list)+1)
        for i in range(len(self.list)):
            if self.list[i].getKey() == pair.getKey():
                return
            if self.list[i].getKey() > pair.getKey():
                self.list.insert(i, pair)
                return
        self.list.append(pair)

    '''
    Returns the sorted symbol table.
    input: - 
    return: sorted symbol table
    '''
    def getList(self):
        return self.list
