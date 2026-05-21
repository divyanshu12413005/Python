d={1:'value','Divyanshu':'key' ,3.5:[1,2,3], (4,5):'tuple as key'}
print(d[3.5]) #accessing value using key
print(d['Divyanshu']) #accessing value using key
print(d, type(d))     #printing entire dictionary
for i in d:
    print(i, ":", d[i])  #printing key and value pairs
    # print(d[i])  #printing value pairs