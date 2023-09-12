text = input()
text_list = []
expl_strength = 0
for letter in text:
    text_list.append(letter)

index = -1
for char in text:
    index += 1
    if char == "":
        expl_strength += int(text_list[index+1])
        for i in range(index, index+expl_strength):
            if text[i] != ">":
                text_list.pop(index)
                expl_strength -= 1
                index -= 1

print(text_list)