
import random


def create_pole(pole, size_y, size_x, empty_cell):
    for i in range(size_y):
        pole.append([])
        for j in range(size_x):
            pole[i].append(empty_cell)


def show_pole(pole):
    print("  1   2   3")
    for i, row in enumerate(pole):
        print(i + 1, end=" ")
        for cell in row:
            print(cell, end=" ")
        print()


def user(pole, size_y, size_x, empty_cell, user_cell):
    while True:
        try:
            pos_y = int(input("Введите строку (1-3): "))
            pos_x = int(input("Введите столбец (1-3): "))

            if pos_y < 1 or pos_y > size_y:
                print("Неправильная строка.")
                continue

            if pos_x < 1 or pos_x > size_x:
                print("Неправильный столбец.")
                continue

            pos_y -= 1
            pos_x -= 1

            if pole[pos_y][pos_x] != empty_cell:
                print("Клетка уже занята.")
                continue

            pole[pos_y][pos_x] = user_cell
            break

        except ValueError:
            print("Введите числа.")


def bot(pole, size_y, size_x, empty_cell, bot_cell):
    empty_cells = []

    for i in range(size_y):
        for j in range(size_x):
            if pole[i][j] == empty_cell:
                empty_cells.append((i, j))

    if empty_cells:
        pos_y, pos_x = random.choice(empty_cells)
        pole[pos_y][pos_x] = bot_cell


def win(pole, cell):
    for row in pole:
        if all(x == cell for x in row):
            return True

    for j in range(3):
        if all(pole[i][j] == cell for i in range(3)):
            return True

    if all(pole[i][i] == cell for i in range(3)):
        return True

    if all(pole[i][2 - i] == cell for i in range(3)):
        return True

    return False


size_y = 3
size_x = 3

pole = []

empty_cell = '[_]'
bot_cell = '[0]'
user_cell = '[X]'

create_pole(pole, size_y, size_x, empty_cell)

print("=== крестики и нолики ===")
print("Ты играешь за X, компьютер за 0.")

while True:
    show_pole(pole)

    user(pole, size_y, size_x, empty_cell, user_cell)

    if win(pole, user_cell):
        show_pole(pole)
        print("Поздравляем, ты победил!")
        break

    if all(cell != empty_cell for row in pole for cell in row):
        show_pole(pole)
        print("Ничья!")
        break

    bot(pole, size_y, size_x, empty_cell, bot_cell)

    if win(pole, bot_cell):
        show_pole(pole)
        print("Компьютер победил!")
        break

    if all(cell != empty_cell for row in pole for cell in row):
        show_pole(pole)
        print("Ничья!")
        break
	