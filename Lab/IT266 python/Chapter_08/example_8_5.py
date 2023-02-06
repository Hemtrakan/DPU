# Program 8.5: Write Python Program to Sort Words in a Sentence in Decreasing
# Order of Their Length. Display the Sorted Words along with Their Length

def sort_words(user_input):
    list_of_words = user_input.split()
    words = list()
    for each_word in list_of_words:
        words.append((len(each_word), each_word))
    words.sort(reverse=True)
    print("After sorting")
    for length, word in words:
        print(f'The word "{word}" is of {length} characters')

def main():
    sentence = input("Enter a sentence ")
    sort_words(sentence)

if __name__ == "__main__":
    main()

# Output
# Enter a sentence Everything you can imagine is real
# After sorting
# The word "Everything" is of 10 characters
# The word "imagine" is of 7 characters
# The word "real" is of 4 characters
# The word "you" is of 3 characters
# The word "can" is of 3 characters
# The word "is" is of 2 characters