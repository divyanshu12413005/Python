x=10
y=20

print("Logical AND:", x < 15 and y > 15) # all conditions must be true
print("Logical AND:", x < 15 and y > 15 and y > 25) # all conditions must be true

print("Logical OR:", x < 15 or y < 15 or y > 25) # at least one condition must be true
print("Logical NOT:", not(x < 15))     # negates the condition
