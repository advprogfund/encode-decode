# Menu and Encoder by Gabriel Fernandez

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
            for i in range(len(rawpass)):
                password += str((int(rawpass[i]) + 7) % 10)     # The encoder performs a Caesar shift of +7 on each digit of the password.
            print("Your password has been encoded and stored!")
        elif (input == 2):
            pass # Decode section for partner to write

        print()

if __name__ == '__main__':
    main()
