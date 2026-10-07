#wap function to print first n lines of the following patterns :-
# ***
# **
# *
#for n = 3 withjout using loop.

def pattern(n):
    if n ==0 :
        return 
    print ( "*" * n)
    pattern ( n-1 )

pattern ( 5 )

