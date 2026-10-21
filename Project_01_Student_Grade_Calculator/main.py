# Student Marks, Average and Grade Calculator
# Concepts: input, type conversion, arithmetic operators, if-elif-else

name = input("Enter student name: ")
mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

# Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
