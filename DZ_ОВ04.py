from abc import ABC, abstractmethod  # Импорт модуля для работы с абстрактными классами

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod  # Декоратор
    def attack(self, monster):  # Абстрактный метод для атаки на монстра
        pass


# Класс Меч
class Sword(Weapon):
    def attack(self, monster):
        print(f"Воин наносит {monster.name} удар мечом.")
        monster.health -= 5
        print(f"Здоровье {monster.name} после удара: {monster.health}")


# Класс Лук
class Bow(Weapon):
    def attack(self, monster):
        print(f"Воин стреляет в {monster.name} из лука.")
        monster.health -= 10
        print(f"Здоровье {monster.name} после выстрела: {monster.health}")


# Класс Воин
class Fighter:
    def __init__(self, weapon=None):
        self.weapon = weapon

    def changeweapon(self, new_weapon):
        self.weapon = new_weapon

    def fight(self, monster):
        # Воин атакует монстра текущим оружием
        if self.weapon:
            self.weapon.attack(monster)
        else:
            print("У воина нет оружия!")


# Класс Монстр
class Monster:
    def __init__(self, name, health):
        self.name = name  # Имя монстра
        self.health = health  # Здоровье монстра
        print(f"{name} с начальным здоровьем: {health}")


# Функция боя
def battle(fighter, monster):
    # бой продолжается пока здоровье монстра больше нуля
    while monster.health > 0:
        fighter.fight(monster)
        if monster.health <= 0:
            print(f"{monster.name} побежден!")
            break


# Создание воина
fighter = Fighter()

# Создание монстров
monster1 = Monster("Монстр 1", health=20)
monster2 = Monster("Монстр 2", health=30)

# Воин выбирает оружие - меч
sword = Sword()
fighter.changeweapon(sword)

# Бой воина с монстром 1
print("Бой Воина с Монстром 1:")
battle(fighter, monster1)

# Воин выбирает оружие - лук
bow = Bow()
fighter.changeweapon(bow)

# Бой воина с монстром 2
print("Бой Воина с Монстром 2:")
battle(fighter, monster2)
