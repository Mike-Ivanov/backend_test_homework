from random import randint

NAME: list = [
    'Звезный лорд',
    'Ракета',
    'Грут',
    'Гамора',
    'Дракс разрушитель',
    'Человек-Паук',
    'Железный человек',
    'Тор',
    'Халк'
]
"""    'Капитан Америка',
    'Соколиный глаз',
    'Доктор Стрэндж',
    'Чеовек-Муравей',
    'Алая ведьма',
    'Расомаха',
    'Чудо-девушка',
    'Хоукай',
    'Капитан Марвел',
    'Локи',
    'Сорвиголова',
    'Черная вдова',
    'Небула',
    'Шторм',
    'Звездный лорд',
    'Мистик',
    'Циклоп'
]"""


class Person:
    def __init__(self,
                 name: str,
                 hp: float,
                 basic_attack: float,
                 basic_protection: float) -> None:
        self.name = name
        self.hp = hp
        self.basic_attack = basic_attack
        self.basic_protection = basic_protection / 100
        self.is_a_life = True

    def set_things(self, things: list):
        """Метод одевает персанажа."""
        for thing in things:
            self.hp += thing.hp
            self.basic_attack += thing.attack
            self.basic_protection += thing.protection
        if self.basic_protection > 1:
            self.basic_protection = 0.99

    def get_damage(self, attacker):
        """Метод вычитания жизни на основании входной атаки."""
        damage = round(attacker.basic_attack
                       - attacker.basic_attack
                       * self.basic_protection, 2)
        self.hp -= damage
        info_damage = '{0} наносит удар по {1} на {2} урона'
        print(info_damage.format(attacker.name, self.name, damage))

        if self.hp <= 0:
            self.is_a_life = False
            print(f'{self.name} - убит!')
        else:
            print(f'У {self.name} осталось {round(self.hp, 2)} жизней')

    def get_player(self) -> str:
        """Метод с выводом общей информации о персонаже."""
        info_player = '{0} - {1} c hp: {2}, атакой: {3}, защитой: {4}.'
        return info_player.format(
            self.__class__.__name__,
            self.name,
            round(self.hp, 2),
            self.basic_attack,
            round(self.basic_protection, 2)
        )


class Paladin(Person):
    def __init__(self,
                 name: str,
                 hp: float,
                 basic_attack: float,
                 basic_protection: float) -> None:
        super().__init__(name, hp * 2, basic_attack, basic_protection * 2)
        if self.basic_protection > 100:
            self.basic_protection = 100

    def __str__(self):
        return self.__class__.__name__


class Warrior(Person):
    def __init__(self,
                 name: str,
                 hp: float,
                 basic_attack: float,
                 basic_protection: float):
        super().__init__(name, hp, basic_attack * 2, basic_protection)

    def __str__(self):
        return self.__class__.__name__


def get_list_players() -> list:
    """Функция  возвращает сгенирированный список игроков."""
    players = []
    for i in range(1, 11):
        hp = randint(40, 100)
        basic_attack = randint(40, 100)
        basic_protection = randint(20, 60)
        if randint(0, 1) == 1:
            players.append(Paladin(
                get_name(),
                hp, basic_attack,
                basic_protection)
            )
        else:
            players.append(Warrior(
                get_name(),
                hp,
                basic_attack,
                basic_protection)
            )
    return players


def get_name() -> str:
    """Функция возвращает рандомное имя."""
    return NAME.pop(randint(1, len(NAME) - 1))


def print_persons(players: list):
    """Функция выводит всех участников турнира."""
    welcome_line = "Поприветствуем игроков: "
    len_welcome_line = len(welcome_line)
    for person in players:
        welcome_line += f'{person.get_player()}\n' + len_welcome_line * ' '
    print(welcome_line)