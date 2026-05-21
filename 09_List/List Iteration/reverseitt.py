l=[10,20,'hello',30,40]
t=len(l)


for i in range(t-1, -1, -1):
    print(l[i])
    
print("")   
    
l=l[-1::-1]
for item in l:
    print(item)

    