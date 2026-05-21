import pickle

file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)
file.close()
