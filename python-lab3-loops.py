# iterating and calculating with loops

# for loops
print("Sum of numbers up to a given integer using for loop:")

n = int(input("Enter a positive integer: "))

sum_for = 0

for i in range(1, n + 1):
    sum_for += i

print("Sum of numbers from 1 to", n, "is:", sum_for)


# while loops
print("\nSum of numbers until sentinel value (0) using while loop:")

sum_while = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    sum_while += num

print("The total sum is:", sum_while)
