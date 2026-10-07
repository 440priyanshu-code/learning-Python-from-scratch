#write a python function to remove a given word
#  from a list .

def rem(l , word ):
    for item in l :
        l.remove (word)
        return l
    
l=  [ " shivam " , " priyanshu ",  "pragya" ,"an"]

print ( rem ( l ,"an"))

