class SymbolTable:
    def __init__(self):
        self.__symbols = []

    '''
    Add a new symbol to the symbol table
    input: symbol - the symbol to be added
    output: -
    '''
    def add(self, symbol):
        self.__symbols.append(symbol)
        self.sort_list(self.__symbols)

    '''
    Search for an element in the symbol table
    input: symbol - the symbol we are looking for
    output: the position of the symbol in the symbol table
    '''
    def search(self, symbol):
        return self.__symbols.index(symbol)

    '''
        Sort a list
        input: list - an unordered list
        output: new_list - the ordered list
    '''
    @staticmethod
    def sort_list(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
