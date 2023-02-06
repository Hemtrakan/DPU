total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        print(f"Sum of all the entered numbers is {total}")
        print(f"Count of total numbers entered {count}")
        print(f"Average is {total / count}")
        break
    else:
        try:
            total += float(num)
        except:
            print("Invalid input")
            continue
    count += 1
