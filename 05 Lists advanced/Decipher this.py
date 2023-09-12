encrypted = input().split()
decrypted = []
decrypted_word = ''
dc_word = []
for word in encrypted:
    i = 0
    last_letter = word[-1]
    first_letter = ''
    while word[i] in '1234567890':
        first_letter += word[i]
        i += 1
    first_letter = chr(int(first_letter))
    dc_word.append(first_letter)
    for letter in word:
        if letter not in '1234567890':
            dc_word.append(letter)
    dc_word[-1] = dc_word[1]
    dc_word[1] = last_letter
    for letter in dc_word:
        decrypted_word += letter
    decrypted.append(decrypted_word)

    decrypted_word = ''
    dc_word.clear()

for word in decrypted:
    print(word, end=' ')
