def replace_comma_with_hyphen(comma_separated_words):
    split_words = comma_separated_words.split(",")
    split_words.sort()
    hyphen_separated_words = "-".join(split_words)
    print(f"Hyphen separated words in ascending order are '{hyphen_separated_words}'")

def main():
    comma_separated_words = input("Enter comma separated words ")
    replace_comma_with_hyphen(comma_separated_words)

if __name__ == "__main__":
    main()


#Output example
#Enter comma separated words global,education
#Hyphen separated words in ascending order are 'education-global'
