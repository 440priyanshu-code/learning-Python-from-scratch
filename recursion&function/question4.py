def greatest(a , b , c):
    if (a>b and a>c):
        return "a is greatest "
    
    if (b>a and b>c):
        return "b is greatest "
    
    if (c>a and c>b):
        return "c is greatest "

a= int ( input ( "enter any number :-"))
b= int ( input ( "enter any number :-"))
c= int ( input ( "enter any number :-"))

print(greatest(a, b, c))