x=10
y=8

print(bin(x)) # Binary representation of x
print(bin(y)) # Binary representation of y

print("Bitwise AND:", bin(x & y), x&y)
print("Bitwise OR:",  bin(x | y), x | y)   
print("Bitwise XOR:", bin(x^y), x ^ y) 
print("Bitwise NOT of x:",bin(~x), ~x) 
print("Left Shift x by 2:", x << 2)  
print("Right Shift x by 2:", x >> 2) 