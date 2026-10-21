# Project 10: Set Operations for Student Subjects
# Syllabus topics: sets, set creation, membership testing, set intersection and union

a = set(input("Student A subjects: ").split())
b = set(input("Student B subjects: ").split())

common = a.intersection(b)
all_subjects = a.union(b)

print("\nCommon subjects:", common)
print("All subjects:", all_subjects)
