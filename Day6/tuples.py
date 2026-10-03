
# 30 Days of Python Learning Challenge
# Day 6: Tuples in Python

# 1. Creating a Tuple
fruits = ("apple", "banana", "cherry", "orange")
print("Fruits:", fruits)

# 2. Accessing Tuple Elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing a Tuple
print("First three fruits:", fruits[0:3])

# 4. Finding the Length of a Tuple
print("Total fruits:", len(fruits))

# 5. Tuple Methods
numbers = (10, 20, 30, 20, 40, 20)

print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# 6. Checking if an Element Exists
print("Is apple in fruits?", "apple" in fruits)

# 7. Looping Through a Tuple
print("All fruits:")
for fruit in fruits:
    print(fruit)

# 8. Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined tuple:", combined)

# 9. Tuple Packing and Unpacking
student = ("Anaswara", 18, "BCA")
name, age, course = student

print("Student Name:", name)
print("Age:", age)
print("Course:", course)

# 10. Single-Element Tuple
single = (100,)
print("Single-element tuple:", single)

# 11. Tuples are Immutable
# Tuples cannot be modified after creation.
# The following line will cause a TypeError:
# fruits[0] = "mango"

print("Day 6 completed: Learning Tuples!")


# Additional Tuple Concepts

# 12. Tuple without parentheses
colors = "red", "green", "blue"
print("Tuple without parentheses:", colors)

# 13. Tuple repetition
repeated = (1, 2, 3) * 2
print("Repeated tuple:", repeated)

# 14. Nested tuples
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Nested element:", nested[0][1])

# 15. Tuple conversion
my_list = [10, 20, 30]
converted = tuple(my_list)
print("List to tuple:", converted)

back_to_list = list(converted)
print("Tuple to list:", back_to_list)

# 16. Built-in functions
values = (10, 20, 30, 40)
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))

# 17. Tuple repetition and comparison
a = (1, 2, 3)
b = (1, 2, 4)
print("Are tuples equal?", a == b)
print("Is a less than b?", a < b)

# 18. Star unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# 19. Empty tuple
empty = ()
print("Empty tuple:", empty)
print("Is empty?", len(empty) == 0)

# 20. Deleting a tuple
temp = (1, 2, 3)
del temp
print("Tuple variable deleted")
