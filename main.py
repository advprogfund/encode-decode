# Menu and Encoder by Gabriel Fernandez

def encode(pwrd):
    # The encoder performs a Caesar shift of +3 on each digit of the password.
    password = ''
    for i in range(len(pwrd)):
        password += str((int(pwrd[i]) + 3) % 10)
    return password

def decode(password):
    """Decoding a password"""
    decoded_password = ""  # An empty string to be added to

    for num in password:
        num = int(num)

        if num > 2:  # Subtracting 3 to decode the number
            decoded_num = num - 3
            decoded_password += str(decoded_num)

        elif 0 <= num <= 2:  # If the number is 0-2, it needs to wrap (eg. 2 - 3 = -1. Instead, 2 + 10 - 3 = 9)
            decoded_num = num + 7
            decoded_password += str(decoded_num)

    return decoded_password


def main():
    cont = True
    password = ''
    while cont:
        # Display the menu to console, and then request input from the user.
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        inp = int(input("Please enter an option: "))
        print()

        if (inp == 3):
            cont = False
        elif (inp == 1):
            takein = True
            password = ''   # Clear old password to encode a new one
            while takein:
                rawpass = str(int(input("Please enter your password to encode: ")))     # Take in password as an integer so it is only numeric, then convert it back to string for later operations.
                if (len(rawpass) == 8):
                    takein = False
                elif (len(rawpass) > 8):    # If password is longer than 8 digits, the program will just truncate it down.
                    rawpass = rawpass[:8]
                    takein = False
                elif (len(rawpass) < 8):    # If password is shorter than 8 digits, the program has no choice but to request new input from the user.
                    print("Password must be eight digits.")
                password = encode(rawpass)
            print("Your password has been encoded and stored!")
        elif (inp == 2):
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")


        print()

if __name__ == '__main__':
    main()
