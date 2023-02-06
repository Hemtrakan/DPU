n = 10
while n > 0:
    print(f"The current value of number is {n}")
    if n == 5:
        print(f"Breaking at {n}")
        n = 10
        continue
    n = n - 1
