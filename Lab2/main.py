from SymbolTable import SymbolTable

st = SymbolTable()

st.add("f")
st.add("b")
st.add("c")
st.add("h")
st.add("a")

print(st.search("f"))
print(st.search("b"))
print(st.search("c"))
print(st.search("h"))
print(st.search("a"))
