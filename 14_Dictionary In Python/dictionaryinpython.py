d={
   'NAme':'Divyanshu',
   'Age':20,
   'Marks':[90, 85, 88], 
   'IsStudent':True,
   'unversity':'IIIT Sonepat'
   }
print(d['NAme'])  #Accessing value using key
print(type(d))  #Printing type of dictionary

print("-----")

d['Age'] = 21  #Modifying value of existing key
print(d)

print("-----")

d['Branch'] = 'CSE'  #Adding new key-value pair
print(d)

print("-----")

del d['IsStudent']  #Deleting key-value pair
print(d)

print("-----")

n=d.pop('Marks')  #Using pop() function to remove key-value pair and return value
print(n)
print(d)

print("-----")

for key in d:
    print(key)  #Printing key 
    
print("-----")   

for i in d:
    print(d[i])  #Printing value using key