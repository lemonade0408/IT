import random


class Shufrator:
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def poschitat(self):
        operation = random.choice(["+", "-", "*"])

        if operation == "+":
            result = self.__number1 + self.__number2
        elif operation == "-":
            result = self.__number1 - self.__number2
        else:
            result = self.__number1 * self.__number2

        return result

    def __str__(self):
        return "Результат: " + str(self.poschitat())


shufrator = Shufrator(8, 4)
print(shufrator)