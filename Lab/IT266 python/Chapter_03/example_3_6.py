fruit_type = input("Enter the Fruit Type:")
if fruit_type == "Oranges":
    print('Oranges are $0.59 a pound')
elif fruit_type == "Apples":
    print('Apples are $0.32 a pound')
elif fruit_type == "Bananas":
    print('Bananas are $0.48 a pound')
elif fruit_type == "Cherries":
    print('Cherries are $3.00 a pound')
else:
    print(f'Sorry, we are out of {fruit_type}')
