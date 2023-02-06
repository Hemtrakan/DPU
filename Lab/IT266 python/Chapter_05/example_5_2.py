def main():
    alphabet = "google"
    index = 0
    print(f"In the string '{alphabet}'")
    for each_character in alphabet:
        print(f"Character '{each_character}' has an index value of {index}")
        index += 1

if __name__ == "__main__":
    main()

#Output example
#In the string 'google'
#Character 'g' has an index value of 0
#Character 'o' has an index value of 1
#Character 'o' has an index value of 2
#Character 'g' has an index value of 3
#Character 'l' has an index value of 4
#Character 'e' has an index value of 5
