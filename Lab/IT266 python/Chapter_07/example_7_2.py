# Program to Illustrate Traversing of key:value Pairs in Dictionaries Using for Loop

currency = {"India": "Rupee", "USA": "Dollar", "Russia": "Ruble", "Japan": "Yen", "Germany": "Euro"}

def main():
    print("List of Countries")
    for key in currency.keys():
        print(key)
    
    print("List of Currencies in different Countries")
    for value in currency.values():
        print(value)

    for key, value in currency.items():
        print(f"'{key}' has a currency of type '{value}'")

if __name__ == "__main__":
    main()

# Output
# List of Countries
# India
# USA
# Russia
# Japan
# Germany
# List of Currencies in different Countries
# Rupee
# Dollar
# Ruble
# Yen
# Euro
# 'India' has a currency of type 'Rupee'
# 'USA' has a currency of type 'Dollar'
# 'Russia' has a currency of type 'Ruble'
# 'Japan' has a currency of type 'Yen'
# 'Germany' has a currency of type 'Euro'