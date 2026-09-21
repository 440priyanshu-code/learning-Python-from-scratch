#check that a tuple cant be change in a python . 

a = (1, 2, 3)

a[0] = 10

print(a)

#ERROR!
#TypeError: 'tuple' object does not support item assignment
