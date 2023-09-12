import re

pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\-_]?[A-Za-z]+(\.[A-Za-z]+)+)+))(\b|(?=\s))"

text = input()

links = re.findall(pattern, text)

for link in links:
    print(link[1])