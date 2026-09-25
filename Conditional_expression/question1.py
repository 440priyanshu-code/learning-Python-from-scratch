#wap to find the greatest of four numbers entered by the user.

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))
num4 = int(input("Enter any number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("The greatest number is", num1)

elif num2 > num1 and num2 > num3 and num2 > num4:
    print("The greatest number is", num2)

elif num3 > num1 and num3 > num2 and num3 > num4:
    print("The greatest number is", num3)

else:
    print("The greatest number is", num4)
    