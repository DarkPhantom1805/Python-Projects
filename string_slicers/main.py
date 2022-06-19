def left(string, position=int):
    return string[: position]

def right(string, position=int):
    return string[len(string) - position: ]    

def mid(string, start_position, steps_from_position):
    st = ""
    st1 = left(string, start_position + steps_from_position)
    st2 = right(string, len(string) - start_position + 1)
    
    for char1 in st1:
        for char2 in st2:
            if char1 == char2:
                st += char1

    return st