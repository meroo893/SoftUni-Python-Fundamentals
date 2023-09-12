text = input()
text_list = [text[0]]
for index in range(1,len(text)):
    if text[index] != text[index-1]:
        text_list.append(text[index])

print("".join(text_list))