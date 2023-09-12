import re

pattern = r"\b_([A-Za-z]+)\b"

text = input()

variables = re.findall(pattern, text)
for variable in variables:
    if variable != variables[-1]:
        print(variable, end=",")
    else:
        print(variable)