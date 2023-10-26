# Joshua Berelson
def encode(password):       #Takes in integer password in a string format and encodes it, shifting each digit by 3
    result = ''
    for i in password:
        result += str((int(i)+3) % 10)
    return result


def decode(password):  # Takes in integer password as a string and decodes it back to original string. -Scott
    password = encode(password)
    result = ''
    for i in password:
        result += str((int(i)+7) % 10)
    return result


def main():          #Main function
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        if user_input == 2:  # Prints out encoded string and decodes it back to the original string. -Scott
            print(f'The encoded password is {encode(password)}, and the original password is {decode(password)}.')

        if user_input == 3:
            exit()


if __name__ == '__main__':
    main()
