words = [ "donkey","good","bad" ]

with open("donkey2.txt", "r") as f :
    content= f.read()

for word in words :
    content = content.replace( word , "#"*len(word))

with open("donkey2.txt", "w") as f :
    f.write(content)
print("Words replaced successfully!")