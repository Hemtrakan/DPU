def common_characters(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")

def main():
    input1 = input("Enter String 1")
    input2 = input("Enter String 2")
    common_characters(input1, input2)

if __name__ == "__main__":
    main()

# Output example
#Character 'o' is found in both the strings
#Character 's' is found in both the strings
#Character 'e' is found in both the strings
