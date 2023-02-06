# Check If the Items in the List Are Sorted in Ascending or Descending
# Order and Print Suitable Messages Accordingly. Otherwise, Print “Items in list are
# not sorted”

def check_for_sort_order(list_items):
    ascending = descending = True
    for i in range(len(list_items) - 1):
        if list_items[i] < list_items[i+1]:
            descending = False
        if list_items[i] > list_items[i+1]:
            ascending = False
    
    if ascending:
        print("Items in list are in Ascending order")
    elif descending:
        print("Items in list are in Descending order")
    else:
        print("Items in list are not sorted")

def main():
    check_for_sort_order([1, 4, 2, 5, 3])

if __name__ == "__main__":
    main()

# Output
# Items in list are not sorted