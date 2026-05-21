w='divyanshu singh chauhan'
t=len(w)
print(t)        #prints the length of string inculuding spaces
w=w[-1::-1]     #reverses the string and stores it back in w

for j in range(t):
        print(w[j]) 
        
        #or
      
      
        print()

for i in range(t-1, -1, -1): 
    print(w[i])  #prints each character of string in reverse order one by one using loop
    