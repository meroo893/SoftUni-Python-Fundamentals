import re


text = ""

while True:
    user_input = input()
    if user_input == '':
        break
    else:
        text+=user_input + " "

extension_pattern = r"\.[a-z]+"

pattern = r"(\bwww\.[A-Za-z0-9\-]+)((\.[a-z]+)+)"
matches = re.findall(pattern, text)
for match in matches:
    print(match[0]+match[1])