# Program to Dynamically Build User Input as a List

list_items = input("Enter list items separated by a space ").split()
print(f"List items are {list_items}")
for m1 in list_items:
    print(m1)
    
    
items_of_list = []
total_items = int(input("Enter the number of items "))
for i in range(total_items):
    item = input("Enter list item: ")
    items_of_list.append(item)

print(f"List items are {items_of_list}")

# Output
# Enter list items separated by a space Asia Europe Africa
# List items are ['Asia', 'Europe', 'Africa']
# Enter the number of items 2
# Enter list item: Australia
# Enter list item: Americas
# List items are ['Australia', 'Americas']