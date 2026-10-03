#wap whcih finds out whether
#  a given name is present in a  list or not.

l= ["harry","shivam","pragya","orry"]
name = input ( "enter your name :-")


if (name in l):
    print( " name is in the list ")

else:
    print( " name is not in the list ")

#...................................................................................................

#Alternate of the above program.


l = ["harry", "shivam", "pragya", "orry"]

name = input("Enter your name: ").strip().lower() #.strip() remove the space from the both soide of the input givem by the user.  
#.lower() converts each and every text to thge lowercase  od the input.

if name in l:
    print("Name is in the list.")
else:
    print("Sorry! Not in the list.")
