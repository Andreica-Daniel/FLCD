from Lab2.symbolTable import Pair
from scanner import Scanner

scanner = Scanner(open("p1.in"))

currentToken = scanner.nextToken()
error = 0
while currentToken:
    tokenClassified = scanner.classifyCodification(scanner.codifyToken(currentToken))
    if tokenClassified == 'lexical error':
        print("LEXICAL ERROR - LINE: " + str(scanner.lineNumber) + ' ,TOKEN: ' + str(scanner.tokenNumber))
        error = 1
    if tokenClassified == 'reserved-word' or tokenClassified == 'operator' or tokenClassified == 'separator':
        scanner.addToPIF(tokenClassified, currentToken, -1)
    else:
        if tokenClassified == 'identifier' or tokenClassified == 'constant':
            pair = Pair(currentToken, 0)
            scanner.addToPIF(tokenClassified, currentToken, scanner.symbolTable.checkIfElementExists(pair))
    currentToken = scanner.nextToken()

f = open("ST.out", "w")
for elem in scanner.symbolTable.getList():
    f.write(elem.getKey() + ' ' + str(elem.getValue()) + '\n')
f.close()

f = open("PIF.out", "w")
for elem in scanner.pif:
    f.write(elem[0] + ' ' + elem[1].getKey() + ' ' + str(elem[1].getValue()) + '\n')
f.close()

if error == 0:
    print("LEXICALLY CORRECT")