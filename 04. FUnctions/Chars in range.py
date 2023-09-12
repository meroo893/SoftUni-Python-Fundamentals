def printCharsInBetw(char_left, char_right):
    chars_in_betw = []
    char_left_ascii = int(ord(char_left))
    char_right_ascii = int(ord(char_right))
    while char_left_ascii < char_right_ascii - 1:
        char_left_ascii += 1
        chars_in_betw.append(chr(char_left_ascii))
    for char in chars_in_betw:
        print(char, end=' ')

printCharsInBetw('!', "z")
