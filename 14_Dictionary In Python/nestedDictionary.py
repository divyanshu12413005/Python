students={
    'Divyanshu':{'University':'IIIT Sonepat', 'Branch':'DSA', 'Year':'2024-2028'},
    'Aditya':{'University':'IIIT Sonepat', 'Branch':'DSA', 'Year':'2024-2028'},
    'Neeraj':{'University':'IIIT Sonepat', 'Branch':'CSE', 'Year':'2024-2028'},
    'Ritik':{'University':'IIIT Sonepat', 'Branch':'IT', 'Year':'2024-2028'},
}

print(students) #Printing entire nested dictionary

print("-----")

print(students['Divyanshu']) #Accessing nested dictionary using key

print("-----")

print(students['Ritik']['Branch']) #Accessing value of nested dictionary using key

print("-----")

print(students['Aditya'] ['Year']) #Printing value of nested dictionary using key

print("-----")

for a,b in students.items():
    print(a,":",b)  #Printing key and value of nested dictionary using for loop

print("-----")

for a,b in students.items():
   print(a,":",b['University'],"&", b['Branch'])  #Printing key and specific value of nested dictionary using for loop
