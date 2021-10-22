from SymbolTable import SymbolTable
from Scanner import Scanner

st = SymbolTable()

st.add("f")
st.add("b")
st.add("c")
st.add("h")
st.add("a")

# print(st.search("f"))
# print(st.search("b"))
# print(st.search("c"))
# print(st.search("h"))
# print(st.search("a"))


myScanner = Scanner(open("p1.in"))

currentToken = myScanner.detectNextToken()
while currentToken:
    print(currentToken)
    currentToken = myScanner.detectNextToken()