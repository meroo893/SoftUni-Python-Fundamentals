def ascii_in_range(lower_char, upper_char):
    asc_lower_char = ord(lower_char)
    asc_upper_char = ord(upper_char)
    for i in range(asc_lower_char + 1, asc_upper_char):
        print(chr(i), end=" ")


lc = input()
uc = input()
ascii_in_range(lc, uc)
