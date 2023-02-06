number = int(input("Enter a number : "))
even = 0
odd = 0
for i in range(number):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Sum of Even numbers are {even} and Odd numbers are {odd}")
