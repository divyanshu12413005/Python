file=open("demow+.text","w+")   #at same w+ read and write 
file.writelines("hello ji\n""Hello World!\n")
file.seek(0)
print(file.read())

file.close()

