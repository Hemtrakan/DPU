x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
try:
    result = x / y
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Executing finally clause")
