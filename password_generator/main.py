import random as r

LETTERS_SMALL = "abcdefghijklmnopqrstuvwxyz"
LETTERS_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "123456789"
SYMBOLS = "!@#$&^&*"

def generate_password(length):
    password = ""
    order = []
    
    for x in range(1, length):
        order.append(x)
    
    r.shuffle(order)

    for x in order:
        repeat = True

        if x == 1 or x == 8 or x == 12:
            while repeat:
                if password.find(r.choice(LETTERS_SMALL)) == -1:
                    password += r.choice(LETTERS_SMALL)
                    repeat = False

        elif x == 2 or x == 7 or x == 11 or x == 13:
            while repeat:
                if password.find(r.choice(LETTERS_CAPS)) == -1:
                    password += r.choice(LETTERS_CAPS)
                    repeat = False

        elif x == 3 or x == 6 or x == 10 or x == 14:
            while repeat:
                if password.find(r.choice(NUMBERS)) == -1:
                    password += r.choice(NUMBERS)
                    repeat = False

        elif x == 4 or x == 5 or x == 9:
            while repeat:
                if password.find(r.choice(SYMBOLS)) == -1:
                    password += r.choice(SYMBOLS)
                    repeat = False

    return password

def main():
    length = int(input("Enter password length between 8 - 14: "))
    password = generate_password(length)
    print(password)

if __name__ == "__main__":
    main()