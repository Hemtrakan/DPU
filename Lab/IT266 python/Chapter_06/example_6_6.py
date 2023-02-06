# Input Five Integers (+ve and −ve). Find the Sum of Negative Numbers,
# Positive Numbers and Print Them. Also, Find the Average of All the Numbers
# and Numbers Above Average
import math
def find_sum(list_items):
    # negative_sum = 0
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0
    for item in list_items:
        if item > 0:
            positive_sum = positive_sum + item
            positive_count += 1
        else:
            negative_sum = negative_sum + item
            negative_count += 1
    
    # average = (positive_sum + negative_sum) / 5
    average_positive_sum = positive_sum / positive_count
    average_negative_sum = negative_sum / negative_count
    print(f"Sum of Positive numbers in list is {positive_sum}")
    print(f"Sum of Negative numbers in list is {negative_sum}")
    # print(f"Average of item numbers in list is {average}")
    print(f"Average_positive_sum of item numbers in list is {average_positive_sum}")
    print(f"Average_negative_sum of item numbers in list is {average_negative_sum}")
    # print("Items above average are")
    # for item in list_items:
    #     if item > average:
    #        print(item)

def main():
    inputNumber = input("Enter Number Positive And Negative : ").split()
    for i in range(len(inputNumber)):
        inputNumber[i] = int(inputNumber[i])
    find_sum(inputNumber)

if __name__ == "__main__":
    main()

# Output
# Sum of Positive numbers in list is 9
# Sum of Negative numbers in list is -6
# Average of item numbers in list is 0.6
# Items above average are
# 4
# 5