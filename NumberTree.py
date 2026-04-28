class Number:
    def __init__(self, value):
        self.up = None
        self.left = None
        self.right = None
        self.value = value

    def append(self, number):
        while True:
            if self.value > number.value:
                if not self.left:
                    self.left = number
                    self.left.up = self
                else:
                    self.left.append(number)
                return
            else:
                if not self.right:
                    self.right = number
                    self.right.up = self
                else:
                    self.right.append(number)
                return

    def level(self):
        if not self.up:
            self.level = 0
        else:
            self.level = self.up.level + 1
        return self.level


def show(number: Number):
    if not number:
        return
    print("\t" * number.level(), "|-", number.value)
    show(number.left)
    show(number.right)

def dfs_check(number: Number):
    print(number.value, end='')
    if number.left:
        print(" -> ", end='')
        dfs_check(number.left)
    if number.right:
        print(" -> ", end='')
        dfs_check(number.right)

number1 = Number(11)
number2 = Number(22)
number3 = Number(18)
number4 = Number(8)
number5 = Number(9)
number6 = Number(6)
number7 = Number(24)
number8 = Number(14)
number9 = Number(26)

number1.append(number2)
number1.append(number3)
number1.append(number4)
number1.append(number5)
number1.append(number6)
number1.append(number7)
number1.append(number8)
number1.append(number9)

show(number1)
dfs_check(number1)
print('\n\n')

import random

numbers = [Number(random.randint(1, 50)) for _ in range(14)]
root = numbers[0]
for node in numbers[1:]:
    root.append(node)

show(root)
dfs_check(root)
