# Write a Function Which Receives a Variable Number of
# Strings as Arguments. Find Unique Characters in Each String

def find_unique(*all_words):
    for each_word in all_words:
        unique_character_list = list(set(each_word))
        print(f"Unique characters in the word {each_word} are {unique_character_list}")

def main():
    find_unique("egg", "immune", "feed", "vacuum", "goddessship")

if __name__ == "__main__":
    main()

# Output
# Unique characters in the word egg are ['e', 'g']
# Unique characters in the word immune are ['m', 'n', 'i', 'u', 'e']
# Unique characters in the word feed are ['d', 'e', 'f']
# Unique characters in the word vacuum are ['m', 'c', 'u', 'a', 'v']
# Unique characters in the word goddessship are ['p', 's', 'o', 'h', 'g', 'i', 'd', 'e']