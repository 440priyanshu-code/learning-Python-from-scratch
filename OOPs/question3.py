#create a claass with a class attribute a ;
#create n object from it and set 'a ' directly 
#using object.a = o . 
#does this change the class attribute ?
class demo :
    a= 4
o = demo () #object 
print ( o.a )

o.a = 0 
print ( o.a )
print ( demo.a )