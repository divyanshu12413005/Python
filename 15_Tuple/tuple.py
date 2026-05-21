t=('Divyanshu', 20, [90, 85, 88])  #Creating a tuple
print(t)  #Printing the tuple
print(t[2])  #Accessing the third element of the tuple

print("-----")

#iterating through a tuple
for i in t:
    print(i)
    
# or using len() and range()
print("-----")
m=len(t)
for i in range(m):
    print(t[i])    