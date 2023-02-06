nterms = int(input('How many terms? '))
current = 0
previous = 1
count = 0
next_term = 0
if nterms <= 0:
    print('Please enter a positive number')
elif nterms == 1:
    print('Fibonacci sequence')
    print('0')
else:
    print("Fibonacci sequence")
    while count < nterms:
        print(next_term)
        current = next_term
        next_term = previous + current
        previous = current
        count += 1
