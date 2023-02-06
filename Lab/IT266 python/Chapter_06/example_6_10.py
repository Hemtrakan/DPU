# Write Python Program to Perform Queue Operations

from collections import deque

def queue_operations():
    queue = deque(["Eric", "John", "Michael"])
    print(f"Queue items are {queue}")
    print("Adding few items to Queue")
    queue.append("Terry")
    queue.append("Graham")
    print(f"Queue items are {queue}")
    print(f"Removed item from Queue is {queue.popleft()}")
    print(f"Removed item from Queue is {queue.popleft()}")
    print(f"Queue items are {queue}")

def main():
    queue_operations()

if __name__ == "__main__":
    main()

# Output
# Queue items are deque(['Eric', 'John', 'Michael'])
# Adding few items to Queue
# Queue items are deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
# Removed item from Queue is Eric
# Removed item from Queue is John
# Queue items are deque(['Michael', 'Terry', 'Graham'])