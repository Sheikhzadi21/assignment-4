def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(i, 'odd')
        else:
            print(i, 'even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1


# This is required to run the main() function when the script is executed
if __name__ == '__main__':
    main()
