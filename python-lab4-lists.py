# Exploring Lists and Their Operations: Perform various list manipulations on a list of numbers, including appending, inserting, removing, and sorting elements.

# Step 1: Create a list of numbers
numbers = [50, 20, 70, 10, 90, 30]
print("Original list:", numbers)

# Step 2: Append a new number to the end
numbers.append(100)
print("After appending 100:", numbers)

# Step 3: Insert 45 at index 2
numbers.insert(2, 45)
print("After inserting 45 at index 2:", numbers)

# Step 4: Remove the first occurrence of 70
numbers.remove(70)
print("After removing 70:", numbers)

# Step 5: Remove and return the element at index 3 using pop()
removed_element = numbers.pop(3)
print("After popping element at index 3:", numbers)
print("Popped element:", removed_element)

# Step 6: Sort the list in ascending order
numbers.sort()
print("After sorting (ascending):", numbers)

# Step 7: Sort the list in descending order
numbers.sort(reverse=True)
print("After sorting (descending):", numbers)

# Step 8: Reverse the list (without sorting)
numbers.reverse()
print("After reversing:", numbers)

# Step 9: Find the length of the list
print("Length of the list:", len(numbers))

# Step 10: Find the maximum and minimum values
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Create a new sorted list without modifying original
original = [40, 10, 80, 30, 60]
sorted_list = sorted(original)
print("\nOriginal list:", original)
print("New sorted list:", sorted_list)
