def main():
    user_string = input("Enter a string: ")
    vowels = 0
    consonants = 0
    blanks = 0
    for each_character in user_string:
        if(each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o' or each_character == 'u' or 
           each_character == 'A' or each_character == 'E' or each_character == 'I' or each_character == 'O' or each_character == 'U'):
            vowels += 1
        elif "a" < each_character <= "z" or "A" < each_character <= "Z":
            consonants += 1
        elif each_character == " ":
            blanks += 1
    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")

if __name__ == "__main__":
    main()

# Output example
#Enter a string: may god bless you
#Total number of Vowels in user entered string is 5
#Total number of Consonants in user entered string is 9
#Total number of Blanks in user entered string is 3
