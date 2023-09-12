import re

sentence = input().lower()
word = r"\b"+input().lower()+r"\b"

count = len(re.findall(word, sentence))

print(count)