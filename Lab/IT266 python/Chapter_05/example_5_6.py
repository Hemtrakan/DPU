def string_processing(user_string):
    word_count = 0
    digit_count = 0
    upper_case_count = 0
    lower_case_count = 0
    for each_char in user_string:
        if each_char.isdigit():
            digit_count += 1
        elif each_char.isspace():
            word_count += 1
        elif each_char.isupper():
            upper_case_count += 1
        elif each_char.islower():
            lower_case_count += 1
        else:
            pass
    print(f"Number of digits in sentence is {digit_count}")
    print(f"Number of words in sentence is {word_count + 1}")
    print(f"Number of upper case letters in sentence is {upper_case_count}")
    print(f"Number of lower case letters in sentence is {lower_case_count}")

def main():
    user_input = input("Enter a sentence ")
    string_processing(user_input)

if __name__ == "__main__":
    main()

#Output example
#Enter a sentence The Eiffel Tower in Paris is 324m tall
#Number of digits in sentence is 3
#Number of words in sentence is 8
#Number of upper case letters in sentence is 4
#Number of lower case letters in sentence is 24
