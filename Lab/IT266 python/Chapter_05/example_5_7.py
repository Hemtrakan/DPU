def case_conversion(user_string):
    convert_case = str()
    for each_char in user_string:
        if each_char.isupper():
            convert_case += each_char.lower()
        else:
            convert_case += each_char.upper()
    print(f"The modified string is {convert_case}")

def main():
    input_string = input("Enter a string ")
    case_conversion(input_string)

if __name__ == "__main__":
    main()


#Output example
#Enter a string ExquiSITE
#The modified string is eXQUIsite
