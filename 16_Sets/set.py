# s={10,20,[30,40]}  #sets do not support mutable data types like list, dictionary etc it only support immutable data types like int, float, string, tuple etc
s={10,20,(30,40)}  #sets support immutable data types like tuple
print(s,type(s))

for i in s:
    print(i)