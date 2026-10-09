#a file contains word "donkey" multiples times 
# wap to replace the word donkey with ##### by updating
#the same file .

with open( "donkey.txt", "r")as f:
    content = f.read()
    print (f"the file contains:- \n {content}")

contentNew = content.replace( "donkey" , "#####")


with open( "donkey.txt", "w") as f:
    content = f.write(contentNew)


print(f"the changed content is :- \n {contentNew}")


print( "changed succesfully !")

