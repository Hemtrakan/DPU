# Write Python Program to Implement Stack Operations

stack = []
stack_size = 3

def display_stack_items():
    print("Current stack items are: ")
    for item in stack:
        print(item)

def push_item_to_stack(item):
    print(f"Push an item to stack {item}")
    if len(stack) < stack_size:
        stack.append(item)
    else:
        print("Stack is full!")

def pop_item_from_stack():
    if len(stack) > 0:
        print(f"Pop an item from stack {stack.pop()}")
    else:
        print("Stack is empty.")

def main():
    push_item_to_stack(1)
    push_item_to_stack(2)
    push_item_to_stack(3)
    display_stack_items()
    push_item_to_stack(4)
    pop_item_from_stack()
    display_stack_items()
    pop_item_from_stack()
    pop_item_from_stack()
    pop_item_from_stack()

if __name__ == "__main__":
    main()

# Output
# Push an item to stack 1
# Push an item to stack 2
# Push an item to stack 3
# Current stack items are:
# 1
# 2
# 3
# Push an item to stack 4
# Stack is full!
# Pop an item from stack 3
# Current stack items are:
# 1
# 2
# Pop an item from stack 2
# Pop an item from stack 1
# Stack is empty.