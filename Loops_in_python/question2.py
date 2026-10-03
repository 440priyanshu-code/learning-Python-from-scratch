#wap to greet all the person names stored in a list 'l'
#  and which starts with S.
#l= ["harrry","soham","suresh","rahul"]


l= ["harrry","soham","Suresh","rahul"]
for name in l:
    if (name.lower().startswith("s")):
        print(f"hello {name}")
