# Project 08: Remove Duplicate Elements from a List
# Syllabus topics: lists, input, type conversion, for loop, if, membership operator

items = list(map(int, input("Enter list elements: ").split()))
unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print("\nOriginal list:", items)
print("List without duplicates:", unique)
