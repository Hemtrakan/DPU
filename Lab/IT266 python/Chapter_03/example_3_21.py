while True:
    try:
        number = int(input("Please enter a number: "))
        print(f"The number you have entered is {number}")
        break
    except ValueError:
        print("Oops! That was no valid number. Try again…")
