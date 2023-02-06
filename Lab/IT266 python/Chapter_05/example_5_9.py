def count_word(word_occurrence, user_string):
    word_count = 0
    for each_word in user_string.split():
        if each_word == word_occurrence:
            word_count += 1
    print(f"The word '{word_occurrence}' has occurred {word_count} times")

def main():
    input_string = input("Enter a string ")
    user_word = input("Enter a word to count its occurrence ")
    count_word(user_word, input_string)

if __name__ == "__main__":
    main()


#Output example
#Enter a string You cannot end a sentence with because because because is a conjunction
#Enter a word to count its occurrence because
#The word 'because' has occurred 3 times
