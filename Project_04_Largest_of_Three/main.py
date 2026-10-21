# Project 04: Largest of Three Numbers
# Syllabus topics: input, type conversion, relational operators, logical operators, if-elif-else

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("\nLargest number:", largest)
