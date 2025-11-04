# ask the user to enter a number
num = float(input("Enter a Number: "))

# check if the number is positive, negative or zero

if num > 0:
    print("The number is positive")

elif num < 0:
    print("The number is negative")

else:
    print("The number is zero")

if num % 2 == 0:
    print("the number is even")
else:
    print("The number is odd")
