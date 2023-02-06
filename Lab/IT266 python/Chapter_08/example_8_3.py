# Write Python Program to Swap Two Numbers Without Using
# Intermediate/Temporary Variables. Prompt the User for Input

def main():
    a = int(input("Enter a value for first number "))
    b = int(input("Enter a value for second number "))
    b, a =5 a, b
    print("After Swapping")
    print(f"Value for first number {a}")
    print(f"Value for second number {b}")

if __name__ == "__main__":
    main()

# Output
# Enter a value for the first number 5
# Enter a value for the second number 10
# After Swapping
# Value for first number 10
# Value for second number 5