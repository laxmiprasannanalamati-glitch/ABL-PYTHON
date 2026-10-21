a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+": result = a + b
elif op == "-": result = a - b
elif op == "*": result = a * b
elif op == "/": result = a / b
else: result = "Invalid operator"
print("\nResult:", result)
