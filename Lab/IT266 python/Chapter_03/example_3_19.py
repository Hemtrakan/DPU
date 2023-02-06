number = int(input('Enter a number > 1: '))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        print(f"i : {i}")
        break
if prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
