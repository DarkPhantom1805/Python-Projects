def alpha_to_num(text):
    code = ""

    for x in text:
        if str(x).isalpha() == True:
            code += str(ord(x))
        else:
            code = code + x

    return code

def shift_right_3(text):
    code = ""
    
    for x in text:
        if str(x).isnumeric() == True:
            code += str(int(x) + 3)
        elif ord(x) > 119:
            code += chr(ord(x) - 23)
        elif ord(x) > 88:
            code += chr(ord(x) - 23)
        elif str(x).isalpha() == True:
            code += chr(ord(x) + 3)
        else:
            code += x

    return code

def multi_tap(text):
    code = ""

    multi_tap = {
        "a" : 2,
        "b" : 22,
        "c" : 222,
        "d" : 3,
        "e" : 33,
        "f" : 333,
        "g" : 4,
        "h" : 44,
        "i" : 444,
        "j" : 5,
        "k" : 55,
        "l" : 555,
        "m" : 6,
        "n" : 66,
        "o" : 666,
        "p" : 7,
        "q" : 77,
        "r" : 777,
        "s" : 7777,
        "t" : 8,
        "u" : 88,
        "v" : 888,
        "w" : 9,
        "x" : 99,
        "y" : 999,
        "z" : 9999
    }

    for x in text:
        if str(x).isalpha():
            code += str(multi_tap.get(x.lower()))
        else:
            code += x

    return code

def main():
    cypher = int(input("""
1 = Alphabets to numbers
2 = Shift alphabets 3 to right
3 = Multi-Tap

Enter Cypher Number:
"""))

    plain_text = input("Enter text to encode: ")

    if cypher == 1:
        encoded = alpha_to_num(plain_text)
        print(encoded)

    elif cypher == 2:
        encoded = shift_right_3(plain_text)
        print(encoded)
    elif cypher == 3:
        encoded = multi_tap(plain_text)
        print(encoded)

if __name__ == "__main__":
    main()