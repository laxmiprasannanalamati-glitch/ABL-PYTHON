# Project 06: Palindrome String Checker
# Syllabus topics: strings, input, if-else, string slicing

text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("\n", text, "is a palindrome.")
else:
    print("\n", text, "is not a palindrome.")
