# Project 02: Electricity Bill Calculator
# Syllabus topics: input, type conversion, variables, arithmetic operators, if-elif-else

units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 + (units - 100) * 2
else:
    bill = 300 + (units - 200) * 3

print("\n--- Electricity Bill ---")
print("Units:", units)
print("Bill Amount:", bill)
