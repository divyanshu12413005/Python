w='divyanshu {} 12413005 {}'.format('hello','iiit')
print(w)  # using format to insert values at {}


t='divyanshu {1} 12413005 {0}'.format('hello','iiit')
print(t)  # using index to change the order of insertion

h='divyanshu {name} 12413005 {institution}'.format(name='hello',institution='iiit')
print(h)  # using named placeholders for insertion

l='divyanshu {b:10} 12413005 {a}'.format(a=100,b=50)
print(l)  # using format to set width of inserted value and aling it to right 

m='divyanshu {b:^10} 12413005 {a}'.format(a=100,b=50)
print(m)  # using format to center align inserted value with width

n='divyanshu {b:<10} 12413005 {a}'.format(a=100,b=50)
print(n)  # using format to right align inserted value with width