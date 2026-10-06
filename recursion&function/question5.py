#wap function to print first n lines of the following patterns :-
# ***
# **
#*
#for n = 3
def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter n: "))
pattern(n)

# OUTPUT:-
# Enter n: 3
# ***
# **
# *
