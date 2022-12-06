# Создайте программу для игры в ""Крестики-нолики"".
import random
import time

def generate_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(' ')
    return board

def print_board(board):
    for i in range(len(board)):
        print(' | '.join(board[i]))
        if i != len(board) - 1:
            print('-' * (len(board) * 4 - 3))

def lottery():
    print('Жеребьевка...', end=' ')
    time.sleep(1)
    player_chosen = bool(random.randint(0, 1))
    print(f'{"Игрок" if player_chosen else "Бот"} ходит первым')
    print('---')
    time.sleep(1)
    return player_chosen

def check_position(position, board):
    if not (0 <= position[0] < len(board) or 0 <= position[1] < len(board[0])):
        return False
    else:
        return board[position[0]][position[1]] == ' '

def check_board_full(board):
    for i in range(len(board)):
        for j in board[i]:
            if j == ' ':
                return False
    return True

def check_win(board):
    for i in board:
        if i.count('X') == len(board) or i.count('O') == len(board):
            return True
    for i in range(len(board)):
        col = [board[j][i] for j in range(len(board))]
        if col.count('X') == len(board) or col.count('O') == len(board):
            return True
    diag1 = [board[i][i] for i in range(len(board))]
    if diag1.count('X') == len(board) or diag1.count('O') == len(board):
        return True
    diag2 = [board[i][-i - 1] for i in range(len(board))]
    if diag2.count('X') == len(board) or diag2.count('O') == len(board):
        return True
    return False

def player_turn(board):
    position = [-1, -1]
    while not check_position(position, board):
        position = [int(input(f'Ваш ход. Введите номер строки (1-{len(board)}): ')) - 1,
                    int(input(f'Введите номер столбца (1-{len(board)}): ')) - 1]
        if not check_position(position, board):
            print('Неверная позиция. Попробуйте снова')
            time.sleep(0.5)
    return position

def bot_turn(board):
    print('Ходит бот')
    time.sleep(0.5)
    position = [-1, -1]
    while not check_position(position, board):
        position = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
    return position

def play_game(board):
    cur_player = lottery()
    while not check_board_full(board):
        if cur_player:
            position = player_turn(board)
        else:
            position = bot_turn(board)
        board[position[0]][position[1]] = 'X' if cur_player else 'O'
        print_board(board)
        print()
        if check_win(board):
            print(f'Игра завершена. {"Вы выиграли. Поздравляем!" if cur_player else "Выиграл бот:("}')
            break
        cur_player = not cur_player
        time.sleep(0.5)
    else:
        print('Никто не выиграл')

BOARD_SIZE = 3

play_game(generate_board(BOARD_SIZE))
