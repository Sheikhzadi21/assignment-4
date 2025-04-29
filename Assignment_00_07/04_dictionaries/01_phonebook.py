def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook dictionary

    while True:
        name = input("Name: ")
        if name == "":
            break  # Stop if the user enters an empty name
        number = input("Number: ")
        phonebook[name] = number  # Add the name and number to the phonebook

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print each name and its number


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Stop if the user enters an empty name
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])  # Print the number associated with the name


def main():
    phonebook = read_phone_numbers()  
    print_phonebook(phonebook)  
    lookup_numbers(phonebook) 

if __name__ == '__main__':
    main()
