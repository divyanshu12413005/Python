def sum(a,b=3):             # Defining a function with a default parameter
    c = a + b                # Function body to calculate sum
    print("The sum is:", c)
    
sum(5)                        # Calling the function with one argument; b takes default value 3
sum(10,20)                    # in this b value overrides the default value