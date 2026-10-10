#wap to rename a file to "renamed_by_python.txt".

with open("file_for_11.txt", "r") as f: 
    content = f.read()



with open("renamed_file_for_11.txt", "w") as f: 
     f.write(content)
