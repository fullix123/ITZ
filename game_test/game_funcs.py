import random
import time

from start_game_here import *


dead_reason = []


#Начальные предметы
replay_items = [The_Blade_of_Extinguished_Souls,The_Ring_of_the_Plague_Omen,Ring_of_Darkness,The_Crown_of_the_Rotting_Throne,The_Bow_of_Bloody_Shadows,The_Eye_of_the_Lost]



#Начальные прелметы x2
start_items = []
start_items.append(The_Blade_of_Extinguished_Souls)
start_items.append(The_Ring_of_the_Plague_Omen)
start_items.append(Ring_of_Darkness)
start_items.append(The_Crown_of_the_Rotting_Throne)
start_items.append(The_Bow_of_Bloody_Shadows)
start_items.append(The_Eye_of_the_Lost)

#Общие функции
def locations(location):
    player.locations.append(location)

def get_valid_input(prompt, valid_options):
    """Запрашивает ввод у пользователя до тех пор, пока не будет введен допустимый вариант."""
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        else:
            print("❗ Неверный ввод. Пожалуйста, выберите один из допустимых вариантов.")





#Локации
def fortress():
    locations("Крепость Расколотой Клятвы 🏰")
    print("Вы попали в Крепость Расколотой Клятвы 🏰")
    choose_fortress = get_valid_input("Перед вами появляется Рыцарь Тысячи Клятв, он предлагает сыграть в 🎲 кубик на его «🪓 Жнец Пепельных Клятв», согласитесь? (да/нет):",["да", "нет"])
    if choose_fortress == "да":
        player_wins = 0
        knight_wins = 0
        move = 1
        print("Правила игры: кубик кидают по очереди, начинает Рыцарь, у кого выпадает большее количество очков - побеждает, игра идет до 3 побед")
        if get_valid_input("Все понятно? (да/нет):",["да", "нет"]) == "да":
            while player_wins < 3 and knight_wins < 3:
                if move % 2 != 0:
                    knight_move = random.randint(1, 6)
                    print("Ходит рыцарь")
                    print(f"🎲 Рыцарь выкинул {knight_move} очков")
                    time.sleep(1.5)
                    move+=1
                elif move % 2 == 0:
                    player_move = random.randint(1, 6)
                    print("Вы ходите")
                    print(f"🎲 Вы выкинули {player_move} очков")
                    time.sleep(1.5)
                    move+=1
                    if player_move == knight_move:
                        print("Ничья!")
                        time.sleep(1.5)
                        player_wins += 1
                        knight_wins += 1
                        print(f'Счет игры: Вы {player_wins} : Рыцаря Тысячи Клятв {knight_wins}')

                    if player_move > knight_move:
                        print("Вы выйграли!")
                        time.sleep(1.5)
                        player_wins += 1
                        print(f'Счет игры: Вы {player_wins} : Рыцаря Тысячи Клятв {knight_wins}')

                    if player_move < knight_move:
                        print("Рыцарь Тысячи Клятв победил!")
                        time.sleep(1.5)
                        knight_wins += 1
                        print(f'Счет игры: Вы {player_wins} : Рыцаря Тысячи Клятв {knight_wins}')
            if player_wins == 3 and knight_wins == 3:
                print("Ничья")
                print("Вы ухродите из крепости и идете дальше по лесу")
                Final_boss()
            elif player_wins == 3:
                if The_Reaper_of_Ashen_Oaths in player.inventory:
                    print("✨Вы уже побеждали Рыцаря, поэтому он вам ничего не дал✨")
                    print("Вы ухродите из крепости и идете дальше по лесу")
                    Final_boss()
                else:
                    print("✨Вы победили Рыцаря Тысячи Клятв! За это он отдает вам 🪓Жнец Пепельных Клятв✨")
                    print(f"{The_Reaper_of_Ashen_Oaths.name}:  {The_Reaper_of_Ashen_Oaths.discription}")
                    player.take_items(The_Reaper_of_Ashen_Oaths)
                    print("Вы ухродите из крепости и идете дальше по лесу")
                    Final_boss()
            else:
                end_game("Вы проиграли Рыцарю Тысячи Клятв, за это он убил вас(")
                dead_reason.append("Вы проиграли Рыцарю Тысячи Клятв, за это он убил вас(")
        else:
            end_game("Рыцарь убил вас за глупость")
            dead_reason.append("Рыцарь убил вас за глупость")
    else:
        print("Вы уходите из крепости и больше не встречаете никого на своем пути")



def casino():
    locations("Казино «Кровавая Рулетка» 🎰")
    print("Вы вошли в Казино «Кровавая Рулетка» 🎰")
    choose_casino = get_valid_input("К вам на встречу выходит Чародей Азарта и предлагает сыграть в блэкджек на «🃏 Колоду Проклятых Тузов», согласитесь? (да/нет):",["да", "нет"])
    if choose_casino == "да":
        player_wins = 0
        enchanter_wins = 0
        move = 1
        print("Правила игры: Игроки по очереди достают карты, их цель получить 21 очко, карты могут быть от 1 до 11 очков. Игроку выдается 1 карта далее он решает брать еще или отказаться, побеждает игрок  получивший количество очков ближе к 21, но НЕ БОЛЕЕ 21!!")
        if get_valid_input("Все понятно? (да/нет): ", ["да", "нет"]) == "да":
            while player_wins < 3 and enchanter_wins < 3:
                print("Вы ходите")
                player_move = random.randint(1, 11)
                while get_valid_input(f"У вас {player_move} очков, брать еще или хватит (еще/хватит):  ",["еще", "хватит"]) == "еще":
                    player_move += random.randint(1, 11)
                    if player_move > 21:
                        print(f"У вас {player_move} очков")
                        break
                    if player_move == 21:
                        print("У вас 21!")
                        break
                print("Чародей ходит")
                enchanter_move = random.randint(1, 11)
                print(f"У Чародея {enchanter_move} очков")
                time.sleep(1)
                while enchanter_move <= 16:
                    print("Чародей берет еще")
                    enchanter_move += random.randint(1, 11)
                    print(f"У Чародея {enchanter_move}")
                    time.sleep(1)
                    if enchanter_move > 21:
                        print(f"У Чародея {enchanter_move} очков")
                        break
                    if enchanter_move == 21:
                        print("У Чародея 21!")
                        break
                print(f"Чародей остановился, у него {enchanter_move} очков, у вас {player_move}")

                if player_move > 21 and enchanter_move > 21:
                    print("Ничья! у вас с Чародеем более 21 очков")
                    player_wins += 1
                    enchanter_wins += 1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif player_move > 21 and enchanter_move <= 21:
                    print("Чародей выйграл")
                    enchanter_wins += 1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif player_move <= 21 and enchanter_move > 21:
                    print("Вы победили!")
                    player_wins += 1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif player_move == 21 and enchanter_move == 21:
                    print("Ничья! у вас с Чародеем 21 очко")
                    player_wins += 1
                    enchanter_wins += 1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif (21 - player_move) > (21 - enchanter_move):
                    print("Чародей выйграл")
                    enchanter_wins+=1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif (21 - player_move) < (21 - enchanter_move):
                    print("Вы победили!")
                    player_wins+=1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
                elif (21 - player_move) == (21 - enchanter_move):
                    print("Ничья у вас одинаковое количество очков")
                    player_wins += 1
                    enchanter_wins += 1
                    print(f'Счет игры: Вы {player_wins} : Чародея Азарта {enchanter_wins}')
            if player_wins == 3:
                if A_Deck_of_Cursed_Aces in player.inventory:
                    print("✨Вы уже побеждали Чародея, поэтому он вам ничего не дал✨")
                    print("Вы вышли из церкви и пошли дальше")
                    Final_boss()
                else:
                    print("✨Вы победили Чародея Азарта! За это он отдает вам 🃏 Колоду Проклятых Тузов✨")
                    print(f"{A_Deck_of_Cursed_Aces.name}:  {A_Deck_of_Cursed_Aces.discription}")
                    player.take_items(A_Deck_of_Cursed_Aces)
                    print()
                    print("Вы уходите из казино и идете дальше")
                    Final_boss()
            else:
                end_game("Вы проиграли Чародею Азарта, за это он убил вас(")
                dead_reason.append("Вы проиграли Чародею Азарта, за это он убил вас(")
        else:
            end_game("Чародей превратил вас в колоду карт, вы погибли")
            dead_reason.append("Вы проиграли Чародею Азарта, за это он убил вас(")
    else:
        end_game("Чародей превратил вас в колоду карт, вы погибли")
        dead_reason.append("Вы проиграли Чародею Азарта, за это он убил вас(")


def church():
    locations("Заброшенная церковь⛪")
    print("Вы зашли в заброшенную церковь⛪")
    choose_church = get_valid_input("Там вы встречаете Монаха Проклятой Клятвы, он предлагает вам сыграть в игру, согласитесь? (да/нет): ",["да", "нет"])
    if choose_church == "да":
        try_counts = 0
        win = 0
        print("Правила игры: Монах загадывает число от 1 до 10, вам нужно угадать это число за 4 попытки")
        if get_valid_input("Все понятно? (да/нет): ", ["да", "нет"]) == "да":
            number = random.randint(1, 10)
            while try_counts < 4 and win == 0:
                attempt = input("Монах загадал число, как вы думаете какое?:  ")
                if attempt == number:
                    win+=1
                    print("Вы угадали число!")
                else:
                    try_counts+=1
                    print("Вы не угадали")
        if win == 1:

            if The_Crystal_of_Destiny in player.inventory:
                print("Вы уже побеждали Монаха, поэтому он вам ничего не дал")
                print("Вы вышли из церкви и пошли дальше")
                Final_boss()
            else:
                print("✨Поздравляю вы победили Монаха, за это он отдает вам 💎 Кристалл Судьбы✨")
                print(f"{The_Crystal_of_Destiny.name}:  {The_Crystal_of_Destiny.description}")
                player.take_items(The_Crystal_of_Destiny)
                print("Вы вышли из церкви и пошли дальше")
                Final_boss()
        else:
            print("Вы проиграли, но монах отпустил вас")
            if get_valid_input("Вы уходите от церкви и видете темный дремучий лес, зайдете? (да/нет):   ", ["да", "нет"]) == "да":
                Final_boss()
            else:
                end_game("Пока вы обходили лес вас убили дикие птицы")
                dead_reason.append("Пока вы обходили лес вас убили дикие птицы")


#Финальный босс

def Final_boss():
    locations("🌲 Темный лес")
    player.battle_items_add()
    print("Вы пришли в 🌲Темный лес")
    print("‼️Вы увидели Владыку Темного леса и он тоже заметил вас, придется с ним биться‼️")
    while True:
        if player.is_alive:
            player.attack(boss)
            print()
            if boss.is_alive:
                print("Владыка нападает❗")
                boss.attack(player)
            else:
                break
        else:
            break
    if player.is_alive:
        end_game("🏆Вы победили финального босса и прошли игру🏆")
        dead_reason.append("Вы не умерли")
    if boss.is_alive:
        end_game("Вы были убили финальным боссом((")
        dead_reason.append("Вы были убили финальным боссом((")



#Начало игры

def start_game():
    print("🌔Добро пожаловать в приключенческую игру в стиле dark fantasy🌔")
    print("Выберите 2 начальных оружий: ")
    for i, item in enumerate(start_items , 1):
        print(f"{i}. {item.name}:  {item.discription}")
    while True:
        try:
            choice = int(input("Введите номер выбранного предмета: ")) - 1
            player.take_items(start_items[choice])
            start_items.pop(choice)
            break
        except:
            print("❗ Неверный ввод. Пожалуйста, выберите один из допустимых вариантов.")

    for i, item in enumerate(start_items , 1):
        print(f"{i}. {item.name}:  {item.discription}")
    while True:
        try:
            choice = int(input("Введите номер выбранного предмета: ")) - 1
            player.take_items(start_items[choice])
            start_items.pop(choice)
            break
        except:
            print("❗ Неверный ввод. Пожалуйста, выберите один из допустимых вариантов.")
    locations("Перекресток после леса")
    firts_choice = get_valid_input("Вы только, что вышли из леса и видите 3 дороги, куда пойдете?   (направо/прямо/налево)  :   ", ["направо", "налево", "прямо"])
    if firts_choice == "направо":
        if get_valid_input("Вы видите казино, будете заходить?  (да/нет)  :   ", ["да", "нет"]) == "да":
            casino()
        else:
            if get_valid_input("Вы проходите казино мимо и идете дальше, и встречаете старца который просит помочь ему, поможете?  (да/нет):   ", ["да", "нет"]) == 'да':
                end_game("Старец заманил вас в ловушку и закалдовал вас")
                dead_reason.append("Старец заманил вас в ловушку и закалдовал вас")
            else:
                if get_valid_input("Вы уходите от старца и приходите к заброшенной церкви, будете заходить?  (да/нет):   ", ["да", "нет"]) == "да":
                    church()
                else:
                    end_game("Больше вы не встретили ни кого на своем пути")
    if firts_choice == "прямо":
        Final_boss()
    if firts_choice == "налево":
        if get_valid_input("Вы видите заброшенную крепость, зайдете?  (да/нет)  :   ", ["да", "нет"]) == "да":
            fortress()
        else:
            print("Вы прошли крепость стороной и пошли дальше")
            print("Вы встретили доброго мудреца который готов отдать вам 1 оружие")
            for i, item in enumerate(start_items, 1):
                print(f"{i}. {item.name}:  {item.discription}")
            choice = int(input("Введите номер выбранного предмета: ")) - 1
            player.take_items(start_items[choice])
            print(f"Вы забрали у старца {start_items.pop(choice)} и пошли дальше")
            start_items.pop(choice)
            Final_boss()





#Запуск игры
def game():
    while True:
        if get_valid_input("Хотите сыграть? (да/нет): ", ["да", "нет"]) == "да":
            start_game()
            if get_valid_input("Хотите сыграть еще? (да/нет): ", ["да", "нет"]) == "да":
                player.hp = 100
                boss.hp = 100
                if dead_reason[0] in [  "Старец заманил вас в ловушку и закалдовал вас",
                                        "Вы были убили финальным боссом((",
                                        "Пока вы обходили лес вас убили дикие птицы",
                                        "Чародей превратил вас в колоду карт, вы погибли",
                                        "Вы проиграли Чародею Азарта, за это он убил вас(",
                                        "Вы проиграли Рыцарю Тысячи Клятв, за это он убил вас(",
                                        "Рыцарь убил вас за глупость"
                                      ]:
                    player.cooldown_items.clear()
                    player.inventory.clear()
                    player.locations.clear()
                    start_items.clear()
                    player.battle_items.clear()
                    player.t = 0
                    for i in replay_items:
                        start_items.append(i)
                    start_game()

                else:
                    if get_valid_input("Хотите оставить предметы? (да/нет): ", ["да", "нет"]) == "да":
                        player.battle_items.clear()
                        start_game()
                    else:
                        player.cooldown_items.clear()
                        player.inventory.clear()
                        player.locations.clear()
                        start_items.clear()
                        player.battle_items.clear()
                        player.t = 0
                        for i in replay_items:
                            start_items.append(i)
                        start_game()
            else:
                break
        else:
            print("❤️Спасибо за игру❤️")
            break

#Конец игры
def end_game(outcome):
    print(f"Игра окончена: {outcome}")
    print(f"💼Собранные предметы: {', '.join(v.name for v in player.inventory)}")
    print(f"🌳Пройденные локации: {', '.join(player.locations)}")
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write("--- Новая игра ---\n")
        file.write(f"💼Собранные предметы: {', '.join(v.name for v in player.inventory)}\n")
        file.write(f"🌳Пройденные локации: {', '.join(player.locations)}\n")
        file.write(f"Результат: {outcome}\n")
        file.write(f"\n")
    return str(outcome)
game()
