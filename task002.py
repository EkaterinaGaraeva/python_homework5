# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

import random

def create_field_for_game():
    field = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    return field

def print_field_for_game(list_with_field):
    for i in range(0, 3):
        print(" ", list_with_field[0+i*3], "|", list_with_field[1+i*3], "|", list_with_field[2+i*3])
        if i < 2:
            print(f" ---|---|---")
    print('\n')

def entering_value(list_with_field):
    print("Введите номер клетки")
    cell_number = input()
    while ((cell_number.isnumeric() != True) or (int(cell_number) < 1) or (int(cell_number) > 9)) \
    or (list_with_field[int(cell_number) - 1] == "x" or list_with_field[int(cell_number) - 1] == "0"):
        print("Номер не верен или клетка уже занята, введите номер клетки в виде цифры от 1 до 9")
        cell_number = input()
    list_with_field[int(cell_number) - 1] = "x"

def computer_running(list_with_field):
    cell_number = random.randint(0, 9)
    while (list_with_field[cell_number - 1] == "x" or list_with_field[cell_number - 1] == "0"):
        cell_number = random.randint(0, 9)
    list_with_field[cell_number - 1] = "0"

def check_win(list_with_field):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_coord:
       if list_with_field[i[0]] == list_with_field[i[1]] == list_with_field[i[2]]:
          return True
   return False

def game():
    field = create_field_for_game()
    print_field_for_game(field)
    win = False
    count = 0
    while win == False or count <= 9:
        entering_value(field)
        print_field_for_game(field)
        win = check_win(field)
        if win == True:
            print(f"Выиграл игрок")
            break
        count += 1
        # print(count)
        if count == 9:
            print(f"Ничья")
            break
        computer_running(field)
        print_field_for_game(field)
        win = check_win(field)
        if win == True:
            print(f"Выиграл компьютр")
            break
        count += 1
        # print(count)
        if count == 9:
            print(f"Ничья")
            break
             
game()
