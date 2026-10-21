# Project 07: Student Marks List Analysis
# Syllabus topics: lists, input, type conversion, list operations, for loop

marks = []

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    total = total + mark

average = total / 5

print("\nMarks:", marks)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
