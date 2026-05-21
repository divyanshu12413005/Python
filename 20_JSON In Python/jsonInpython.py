import json
d={'name': 'Alice', 'age': 30, 'city': 'New York'} 
print(type(d)) 

#diff in json and python dictionary is that in json keys and string values are in double quotes
# Convert Python dictionary to JSON string
f = json.dumps(d)
print(f,type(f))


l=['Apple', 'Banana', 'Cherry']
print(type(l))
c=json.dumps(l)
print(c,type(c))

y = json.loads(c)   # Convert JSON string back to Python dictionary
                    
print(y,type(y))