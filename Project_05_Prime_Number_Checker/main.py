# Project 05: Prime Number Checker
# Syllabus topics: input, type conversion, variables, arithmetic operators, if, for, break

n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("\n", n, "is a prime number.")
else:
    print("\n", n, "is not a prime number.")
