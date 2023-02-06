# Program to Populate Tuple with User-Entered Items

tuple_items = ()
total_items = int(input("Enter the total number of items: "))
for i in range(total_items):
    user_input = int(input("Enter a number: "))
    tuple_items += (user_input,)
print(f"Items added to tuple are {tuple_items}")

list_items = []
total_items = int(input("Enter the total number of items: "))
for i in range(total_items):
    item = input("Enter an item to add: ")
    list_items.append(item)
items_of_tuple = tuple(list_items)
print(f"Tuple items are {items_of_tuple}")

# Output
# Enter the total number of items: 4
# Enter a number: 4
# Enter a number: 3
# Enter a number: 2
# Enter a number: 1
# Items added to tuple are (4, 3, 2, 1)
# Enter the total number of items: 4
# Enter an item to add: 1
# Enter an item to add: 2
# Enter an item to add: 3
# Enter an item to add: 4
# Tuple items are ('1', '2', '3', '4')