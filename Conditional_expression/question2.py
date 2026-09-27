#wap to find out whether a student has passed or failed if it requires a 
#total of 40% and at least 33% in each subject has passed or failed if it requires a take marks  as an input from the user.

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total_percentage = ((marks1 + marks2 + marks3) / 300) * 100
print ( "total percentage is :-",total_percentage)


if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")