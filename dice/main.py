import random
from tokenize import Triple

def diceroll():
    face = random.randint(1, 6)
    return face

def main():
    x = ''
    roll = True

    while roll:
        x = input("Roll dice? Yes or No : ").lower()
        
        if x == "yes" or x == "y":
            print(diceroll())
        elif x == "no" or x == 'n':
            roll = False
        else:
            print("Invalid Input!")
        
if __name__ == "__main__":
    main()