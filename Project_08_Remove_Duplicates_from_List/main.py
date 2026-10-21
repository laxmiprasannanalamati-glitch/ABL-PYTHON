items = list(map(int, input("Enter list elements: ").split()))
unique = []
for item in items:
    if item not in unique: unique.append(item)
print("\nOriginal list:", items)
print("List without duplicates:", unique)
