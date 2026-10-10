#wap to find out the line number 
#where python is present from question 6 .

with open( "log.txt") as f:
    lines = f.readlines()
lineno =1
for line in lines :   
    if ("python" in line):
        print ( f" the word python is present ,line no.:-{lineno}")
        break 
    lineno += 1

else :
    print ( " the word python is not present ")

 