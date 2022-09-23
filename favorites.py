import math

choice=10
while choice != 0:
    choice = int(input("Press 1 to find the average of three numbers. Press 2 for the square root of two numbers/what the product of your first chosen number to the power of two is. "))
    if choice == 1:
        num = int(input("Please enter the first number"))
        num2 = int(input("Please enter the second number"))
        num3 = int(input("Please enter last number"))
        print((num + num2 + num3)/3)
    elif choice == 2:
        num = int(input("Please enter first number"))
        num2 = int(input("Please enter seond number"))
        print("The square root of the first numbers is", (math.sqrt(num)), "and the second number's square root is", (math.sqrt(num2)))
              
