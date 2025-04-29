INCHES_IN_FOOT: int = 12

def main():
    # Input: Ask user to enter feet
    feet: float = float(input("Enter number of feet: "))
    
    # Process: Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT

    # Output: Print the result
    print("That is", inches, "inches!")

# Call main() if the file is run directly
if __name__ == '__main__':
    main()