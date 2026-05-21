s={10,20,'Divyanshu',40.5,10}
s.discard('Divyanshu')  #discard function removes a specified value from the set it does not raise an error if the value is not found
print(s) 

print(s.discard(100))   #this will not raise an error because 100 is not present in the set
