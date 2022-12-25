def print_field(matrix):
    print(' ', 0, 1, 2, sep="  ")
    print(0, *matrix[0], sep="  ")
    print(1, *matrix[1], sep="  ")
    print(2, *matrix[2], sep="  ")


def check_winner(matrix):
    # проверяем строки
    if matrix[0].count('x') == 3:
        return 1
    if matrix[1].count('x') == 3:
        return 1
    if matrix[2].count('x') == 3:
        return 1

    if matrix[0].count('o') == 3:
        return 2
    if matrix[1].count('o') == 3:
        return 2
    if matrix[2].count('o') == 3:
        return 2

    # проверяем столбцы
    if matrix[0][0] == matrix[1][0] == matrix[2][0] == 'x':
        return 1
    if matrix[0][1] == matrix[1][1] == matrix[2][1] == 'x':
        return 1
    if matrix[0][2] == matrix[1][2] == matrix[2][2] == 'x':
        return 1

    if matrix[0][0] == matrix[1][0] == matrix[2][0] == 'o':
        return 2
    if matrix[0][1] == matrix[1][1] == matrix[2][1] == 'o':
        return 2
    if matrix[0][2] == matrix[1][2] == matrix[2][2] == 'o':
        return 2

    # проверяем диагонали
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x':
        return 1
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'x':
        return 1

    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'o':
        return 2
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'o':
        return 2

    return


field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

side = 1  # первым ходит Крестик
step_count = 0
winner = None

print("Добро пожаловать в игру Крестики-Нолики!")

while winner is None:
    print_field(field)

    if side == 1:
        print("Ходит Крестик.")
    else:
        print("Ходит Нолик.")

    # игрок делает ход
    while True:
        try:
            x = int(input("X: "))
            y = int(input("Y: "))
        except ValueError:
            print("Координаты должны быть числами. Попробуйте ещё раз.")
            continue

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[y][x] == '-':
                break
            else:
                print("Данное поле уже занято.")
                print("Сделайте ход в пустое поле.")
        else:
            print("Неверные координаты.")
            print("Каждая координата должна быть числом 0, 1 или 2.")
            print("Попробуйте ещё раз.")

    if side == 1:
        field[y][x] = 'x'
        side = 2  # передаем ход Нолику
    else:
        field[y][x] = 'o'
        side = 1

    step_count += 1

    # начинаем проверку победы только после 5 сделанных ходов
    if step_count >= 5:
        winner = check_winner(field)

    # проверка на ничью
    if step_count == 9 and winner is None:
        winner = 0

print_field(field)

print("Игра завершена. Результат:")

if winner == 1:
    print(f"Победил Крестик на {step_count} ходу")
elif winner == 2:
    print(f"Победил Нолик на {step_count} ходу")
else:
    print(f"Ничья. Победила дружба!")
