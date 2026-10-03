
# 30 Days of Python Learning Challenge
# Day 7: Sets in Python

# 1. Creating a Set
fruits = {"apple", "banana", "cherry", "orange"}
print("Fruits:", fruits)

# 2. Creating an Empty Set
empty_set = set()
print("Empty set:", empty_set)

# 3. Sets Do Not Allow Duplicates
numbers = {1, 2, 3, 2, 4, 3, 5}
print("Unique numbers:", numbers)

# 4. Adding Elements
fruits.add("mango")
print("After adding:", fruits)

# 5. Adding Multiple Elements
fruits.update(["grapes", "watermelon"])
print("After update:", fruits)

# 6. Removing Elements
fruits.remove("banana")
print("After remove:", fruits)

# 7. Discarding Elements
fruits.discard("pineapple")  # No error if absent
print("After discard:", fruits)

# 8. Removing an Arbitrary Element
removed = fruits.pop()
print("Popped element:", removed)
print("After pop:", fruits)

# 9. Checking Membership
print("Is apple present?", "apple" in fruits)

# 10. Set Length
print("Number of fruits:", len(fruits))

# 11. Iterating Through a Set
print("All fruits:")
for fruit in fruits:
    print(fruit)

# 12. Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Union using method:", A.union(B))

# 13. Intersection
print("Intersection:", A & B)
print("Intersection using method:", A.intersection(B))

# 14. Difference
print("A - B:", A - B)
print("Difference using method:", A.difference(B))

# 15. Symmetric Difference
print("Symmetric difference:", A ^ B)
print("Using method:", A.symmetric_difference(B))

# 16. Subset
X = {1, 2}
Y = {1, 2, 3, 4}
print("X is a subset of Y:", X.issubset(Y))

# 17. Superset
print("Y is a superset of X:", Y.issuperset(X))

# 18. Disjoint Sets
P = {1, 2, 3}
Q = {4, 5, 6}
print("Are P and Q disjoint?", P.isdisjoint(Q))

# 19. Set Comparison
print("Are A and B equal?", A == B)

# 20. Copying a Set
copied_set = A.copy()
print("Copied set:", copied_set)

# 21. Clearing a Set
temp = {10, 20, 30}
temp.clear()
print("After clearing:", temp)

# 22. Set Comprehension
squares = {x ** 2 for x in range(1, 6)}
print("Squares:", squares)

# 23. Converting List to Set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(my_list)
print("List to set:", unique_values)

# 24. Immutable Set (frozenset)
fixed = frozenset([1, 2, 3, 4])
print("Frozen set:", fixed)

# 25. Finding Minimum, Maximum and Sum
values = {10, 20, 30, 40}
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))

print("Day 7 completed: Learning Sets!")
