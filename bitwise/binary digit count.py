class Num:
    def __init__(self, number: int):
        self.number = number

    def to_bin_list(self):
        temp = []
        while True:
            temp.append(self.number % 2)
            self.number = self.number // 2
            if self.number == 0:
                break
        temp.reverse()
        return temp


n = Num(int(input()))
binary = n.to_bin_list()
"""
b = int(input())
count = 0
for bit in binary:
    if bit == b:
        count += 1

print(count)"""

"""index = int(input())
print(binary[-index])"""