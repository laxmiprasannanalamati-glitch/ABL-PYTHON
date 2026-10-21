# Project 09: Student Details Using Tuple
# Syllabus topics: tuples, input, tuple indexing, tuple unpacking

name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")

student = (name, roll, branch)
student_name, student_roll, student_branch = student

print("\n--- Student Details ---")
print("Name:", student_name)
print("Roll Number:", student_roll)
print("Branch:", student_branch)
