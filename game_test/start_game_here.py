import random
from game_funcs import *








class Player:
    def __init__(self,name,hp, inventory, locations):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.locations = locations

    #Вспомогательные массивы
    cooldown_items = []
    battle_items = []
    t = 0
    real_hp = 0


    #Добавление предметов которые используются в битве
    def battle_items_add(self):
        global battle_items
        for i in self.inventory:
            self.battle_items.append(i)

    #Получение урона
    def take_damage(self, damage):
        self.hp -= damage

    #Выбор предмета
    def choose_item(self):
        global cooldown_items, t, battle_items
        if self.t == 2:
            try:
                print(f"{self.cooldown_items[0].name} опять можно пользоваться!⌛")
            except:
                print(f"{self.cooldown_items[1].name} опять можно пользоваться!⌛")
            self.battle_items.append(self.cooldown_items[0])
            self.cooldown_items.pop(0)
            self.t = 1
        print("Выберите предмет которым будете атаковать: ")
        for i, item in enumerate(self.battle_items, 1):
            print(f"{i}. {item.name}:  {item.discription}")
        while True:
            try:
                choice = int(input("Введите номер выбранного артефакта: ")) - 1
                #Добавление предмета в перезарядку
                self.cooldown_items.append(self.battle_items[choice])
                self.battle_items.pop(choice)
                self.t += 1
                return self.cooldown_items[-1]
            except:
                print("❗ Неверный ввод. Пожалуйста, выберите один из допустимых вариантов.")


    #Атака
    def attack(self,target):
        item = self.choose_item()
        if item.type == "crit15":
            damage = item.crit_15()
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку")



        #Проверка модификатора предмета


        elif item.type == "crit2":
            damage = item.crit_2()
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "heal5":
            item.heal_5()
            damage = item.damage
            target.take_damage(damage)
            print(f"Вы излечили себя на 10hp, {self.hp - 5} -> {self.hp}")
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "heal10":
            item.heal_10()
            damage = item.damage
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            print(f"Вы излечили себя на 10hp, {self.hp - 10} -> {self.hp}")
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "heal20":
            item.heal_20()
            print(f"Вы излечили себя на 20hp, {self.hp - 20} -> {self.hp}")
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "second_attack":
            damage = item.second_attack()
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "miss100":
            item.miss_100()
            damage = item.damage
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")


        elif item.type == "miss50":
            item.miss_50()
            damage = item.damage
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {item.damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")

        #Если у предмета нету модификатора
        else:
            damage = item.damage
            print()
            target.take_damage(damage)
            print(f'Вы атакуете {target.name} и наносите {damage} урона, {target.name}: {target.hp} hp')
            try:
                print(f"{self.cooldown_items[1].name} ушел в перезарядку⌛")
            except:
                print(f"{self.cooldown_items[0].name} ушел в перезарядку⌛")

    #Получение предмета
    def take_items(self, items):
        self.inventory.append(items)

    #Проверка жив ли игрок
    @property
    def is_alive(self):
        return self.hp > 0


class Items:
    def __init__(self, name, damage, type,   description):
        self.name = name
        self.damage = damage
        self.discription = description
        self.type = type



    #Модификаторы предметов

    #Усиленный удар в 1.5 раза с шансом 30%
    def crit_15(self):
        if random.randint(1,10) >= 1:
            crit_damage = self.damage * 1.5
            print(f"Вы наложили яд, урон ={crit_damage}")
            return crit_damage
        else:
            return self.damage

    #Усиленный удар в 2 раза с шансом 50%
    def crit_2(self):
        if random.randint(1, 10) >= 5:
            crit_damage = self.damage * 2
            print(f"Выпал крит урон = {crit_damage}")
            return crit_damage
        else:
            return self.damage


    #Вторая атака c увеличеным уроном с шансом 30%
    def second_attack(self):
        if random.randint(1, 10) >= 8:
            double_attack = self.damage + self.damage*0.6
            print(f'Вы выпустили 2 стрелы урон стал => {round(double_attack)}')
            return round(double_attack)
        else:
            return self.damage

    #Противник промахнется при следующей атаке
    def miss_100(self):
        boss.miss = 1

    #Шанс уворота 50%
    def miss_50(self):
        if random.randint(1, 10) >= 5:
            boss.miss = 1
        else:
            pass

    # Излечение на 5 хп
    def heal_5(self):
        player.hp+=5

    #Излечение на 10 хп
    def heal_10(self):
        player.hp+=10
        print(f'Вы изличили себя на 10 hp')

    # Излечение на 20 хп
    def heal_20(self):
        player.hp+=20
        print(f'Вы изличили себя на 20 hp')


    #Излечение на 5 хп и шанс уворота 50%
    def miss50_heal5(self):
        player.hp += 5
        print(f'Вы изличили себя на 5 hp')
        if random.randint(1, 10) >= 5:
            boss.miss = 1
        else:
            pass




class Boss:
    def __init__(self,name= "Владыка темного леса",  hp = 150, inventory = [], miss = 0 ):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.miss = miss


    #Получение урона
    def take_damage(self, damage):
        self.hp -= damage

    #Атака случайным предметом
    def attack(self,target):
        item = random.choice(self.inventory)
        damage = item.damage
        if self.miss == 1:
            print(f"Вы увернулсь от атаки!")
            print()
            self.miss = 0
        else:
            target.take_damage(damage)
            print(f'{self.name} атакует вас и наносит вам {damage} урона, при помощи {item.name}, теперь у вас : {target.hp} hp')
            print()

    #Получение предмета
    def take_items(self, items):
        self.inventory.append(items)

    #Проверка жив ли босс
    @property
    def is_alive(self):
            return self.hp > 0


#Создание босса и игрока
boss = Boss()
player = Player("Аркадий", 100, [], [])


#Создание предметов
The_Blades_of_the_Bone_Judge = Items("⚔️ Клинки Костяного Судьи", 17, "crit2",  "Эти клинки способны нанести двойной урон с 50% шансом, урон = 17.")
The_Blade_of_Extinguished_Souls = Items("🗡️ Клинок Погасших Душ", 13, "default", "Обычные клинки с неплохим уроном, урон = 13.")
The_Ring_of_the_Plague_Omen = Items("🌑 Перстень Чумного Знамения",  6, "miss50" , "Перстень позволяет увернуться от следующей атаки с 50% шансом, урон = 6.")
Ring_of_Darkness = Items("💍 Кольцо Тьмы", 5, "heal5" , "Кольцо излечит вас на 5hp, урон = 5.")
The_Crown_of_the_Rotting_Throne = Items("👑 Корона Гниющего Престола", 0, "miss100" , "Корона дает уклонение 100% из-за чего следущая атака не насет вам урона, урон = 0.")
The_Bow_of_Bloody_Shadows = Items("🏹 Лук Кровавых Теней", 9, "second_attack" , "Лук с 30% шансом выпустит вторую стрелу с 60% уроном, урон = 9.")
The_Eye_of_the_Lost = Items("🧭 Око Заблудших", 0, "heal10" , "Около вылечит на 10hp, урон = 0.")
The_Amulet_of_the_Whispering_Graves = Items("🧿 Амулет Шёпота Могил", 0, "miss50_heal5" , "Амулет восстонавливет 5hp и с 50% шансом увернется от следующей атаки, урон = 0.")
Tom_Necrogymnov = Items("📕 Том Некрогимнов", 11, "crit15" , "Том Некрогимнов с 30% шансом накладывает яд, который нанесет 70% от урона, урон = 11")
The_Crystal_of_Destiny = Items("💎 Кристалл Судьбы", 15, "heal15" ,"Кристалл может восстановить 15hp, урон = 15  .")
The_Reaper_of_Ashen_Oaths = Items("🪓 Жнец Пепельных Клятв", 22, "crit2", "Жнец может нанести двойной урон с 50% шансом, урон = 18.")
A_Deck_of_Cursed_Aces = Items("🃏 Колода Проклятых Тузов", 19, "miss100" , "Колода Тузов позволяет увернуться от следуещей атаки с 100% шансом, урон = 15 .")

#Предметы босса
The_Horn_Of_The_Rotting_Deer = Items("🦴 «Рог Гниющего Оленя»", 21, "boss" , "Этот рог выглядит так, словно вырос из гниющей земли и впитал в себя смерть леса. Его поверхность шероховата, с трещинами и пятнами плесени, а конец слегка разветвлён, напоминая когти или клыки. Внутри рога слышны слабые стоны — будто древний зверь не успел уйти в покой.")
The_Claws_of_the_Night_Owl = Items("🦉 Когти Ночной Совы", 20, "boss" , "Кинжалы напоминают изогнутые когти ночной совы: острые, как клык, с лёгким блеском в темноте. Рукояти обтянуты переплётёнными перьями и сухожилиями, ощущаются холодными и живыми, будто в них заключён дух хищника.")
The_Bow_of_the_Ghostly_Doe = Items("🏹 Лук Призрачной Лани", 19, "boss" , "Лук Призрачной Лани излучает слабое серебристое свечение, словно его древесина пропитана лунным светом. Его изгибы лёгкие, но невероятно прочные, а тетива дрожит, будто сама природа дышит вместе с владельцем.")
Spiders_Braided_Whip = Items("🕸 Плетёный Кнут Паука", 18 , "boss" , "Кнут выглядит почти невидимым в темноте, его шелковистые нити едва мерцают при свете луны. При взмахе он издаёт шепчущий звук, похожий на шорох паутины. Рукоять изогнута из костей, покрыта чёрной смолой, и кажется, что кнут живёт своей собственной волей.")



#Добавление предметов боссу
boss.take_items(The_Horn_Of_The_Rotting_Deer)
boss.take_items(The_Claws_of_the_Night_Owl)
boss.take_items(The_Bow_of_the_Ghostly_Doe)
boss.take_items(Spiders_Braided_Whip)

