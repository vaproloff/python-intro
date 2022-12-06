# Создайте программу для игры с конфетами человек против человека. Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
import time

def lottery(player1_name, player2_name):
    print('Жеребьевка...', end=' ')
    time.sleep(1)
    player_chosen = random.randint(1, 2)
    print(f'{player1_name if player_chosen == 1 else player2_name} ходит первым')
    print('---')
    time.sleep(1)
    return player_chosen

def player_turn(player_name, max_take, candies_quantity):
    take = 0
    while not (0 < take <= max_take and candies_quantity - take >= 0):
        take = int(input(f'{player_name}. Ваш ход (введите количество конфет от 1 до {max_take}): '))
        if take > max_take:
            print('Это слишком много конфет')
        if take < 1:
            print('Нужно взять хотя бы одну конфету')
        if candies_quantity - take < 0:
            print('Вы хотите взять больше конфет, чем осталось на столе')
        time.sleep(0.5)
        print('---')
    return take

def bot_turn(candies_quantity, max_take, is_super):
    if is_super:
        take = candies_quantity - (candies_quantity // (max_take + 1)) * (max_take + 1) or 1
    else:
        take = random.randint(1, min(max_take, candies_quantity))
    print(f'Бот взял конфет: {take}')
    print('---')
    time.sleep(0.5)
    return take

def play_game(candies_quantity, max_take, mode):
    if mode == 1:
        cur_player = lottery('Игрок 1', 'Игрок 2')
    else:
        cur_player = lottery('Игрок', 'Бот')
    while candies_quantity > 0:
        print(f'На столе осталось конфет: {candies_quantity}')
        time.sleep(0.5)
        if mode == 1:
            take = player_turn('Игрок 1' if cur_player == 1 else 'Игрок 2', max_take, candies_quantity)
        else:
            if cur_player == 1:
                take = player_turn('Игрок', max_take, candies_quantity)
            else:
                take = bot_turn(candies_quantity, max_take, True if mode == 3 else False)
        candies_quantity -= take
        if candies_quantity > 0:
            cur_player = 2 if cur_player == 1 else 1
        else:
            print(f'На столе не осталось конфет')
            if mode == 1:
                print(f'{"Игрок 1" if cur_player == 1 else "Игрок 2"} победил. Поздравляем!')
            else:
                print(f'{"Игрок" if cur_player == 1 else "Бот"} победил. Поздравляем!')

CANDIES_QUANTITY = 2021
MAX_TAKE = 28

print('1. Человек VS. Человек.\t 2. Человек VS. Бот.\t 3. Человек VS. Супербот')
game_mode = int(input('Выберите режим игры (1, 2 или 3): '))
print('---')
if 0 < game_mode <= 3:
    play_game(CANDIES_QUANTITY, MAX_TAKE, game_mode)
else:
    print('Такого режима нет')