def main():
    user_string = input("Enter a string: ")
    count_character = 0
    for each_character in user_string:
        count_character += 1
    print(f"The length of user entered string is {count_character} ")

if __name__ == "__main__":
    main()

#Output example
#Enter a string: To answer before listening that is folly and shame
#The length of user entered string is 50
