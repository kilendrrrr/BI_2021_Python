a = input("Enter a: ")
math_operation = input("math operation: ")
b = input("Enter b: ")

a = float(a)
b = float(b)

if math_operation == "+":
        result = a + b
elif math_operation == "-":
        result = a - b
elif math_operaton == "*":
        result = a * b
elif math_operation == "/":
        result = a /b
elif math_operation == "^":
        result = a ^ b
        
print("Result:", result)
        
