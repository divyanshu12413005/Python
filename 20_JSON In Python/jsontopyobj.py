import json
j='{"name": "Alice", "age": 30, "city": "New York"}'
print(type(j))

x= json.loads(j)
print(x,type(x))

for a in x:
    print(a,':',x[a])     # a represents keys in dictionary and x[a] represents values in dictionary