# Program to Dynamically Build User Input as a List

def main():
    print("Method 1: Building Dictionaries")
    build_dictionary = {}
    for i in range(0, 2):
        dic_key = input("Enter key ")
        dic_val = input("Enter val ")
        build_dictionary.update({dic_key: dic_val})

    print(f"Dictionary is {build_dictionary}")

    print("Method 2: Building Dictionaries")
    build_dictionary = {}
    for i in range(0, 2):
        dic_key = input("Enter key ")
        dic_val = input("Enter val ")
        build_dictionary[dic_key] = dic_val
    print(f"Dictionary is {build_dictionary}")

    print("Method 3: Building Dictionaries")
    build_dictionary = {}
    i = 0
    while i < 2:
        dict_key = input("Enter key ")
        dict_val = input("Enter val ")
        build_dictionary.update({dict_key: dict_val})
        i = i + 1
    print(f"Dictionary is {build_dictionary}")

if __name__ == "__main__":
    main()

# Output
# Method 1: Building Dictionaries
# Enter key microsoft
# Enter val windows
# Enter key canonical
# Enter val ubuntu
# Dictionary is {'microsoft': 'windows', 'canonical': 'ubuntu'}
# Method 2: Building Dictionaries
# Enter key apple
# Enter val macos
# Enter key canonical
# Enter val ubuntu
# Dictionary is {'apple': 'macos', 'canonical': 'ubuntu'}
# Method 3: Building Dictionaries
# Enter key microsoft
# Enter val windows
# Enter key apple
# Enter val macos
# Dictionary is {'microsoft': 'windows', 'apple': 'macos'}