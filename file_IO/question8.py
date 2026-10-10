# wap to make a copy of text file "this.txt" .

# WAP to make a copy of the text file "this.txt"

with open("this.txt", "r") as f: #"this.txt" → Opens the original file and reads its content.
    content = f.read()  #content = f.read() → Stores the content in the variable content.

with open("this_copy.txt", "w") as f: #"this_copy.txt" → Creates a new file without the extra space.
    f.write(content) #f.write(content) → Copies the original content into the new file.

print("The copy of this.txt file has been generated successfully!")
