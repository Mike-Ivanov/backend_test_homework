import operator
from random import randint, choice

THINGS: list = [
    'Мантия невидимости',
    'Сапоги скороходы',
    'Магическое кольцо',
    'Перчатки силы',
    'Пояс прочности',
    'Роба магов',
    'Молот Тора',
    'Волшебный посох',
    'Лезвия атаки',
    'Кольчуга',
    'Клеймор',
    'Перчатки сокрости',
    'Маска ужаса',
    'Скипетр ужаса',
    'Нарукавник',
    'Талисман силы',
    'Ботинки силы',
    'Посох забвения',
    'Непробивной щит',
    'Медальон мужества',
    'Маска вампира',
    'Мерцающий плащ',
    'Посох сил',
    'Жезл атоса',
    'Солнечный гребень',
    'Багровая кираса',
    'Латы штурмовика',
    'Темный клинок'
    ]


class Thing:
    def __init__(self, name: str) -> None:
        self.name = name
        self.protection = randint(1, 10) * 0.01
        self.attack = randint(20, 60)
        self.hp = randint(20, 60)

    def print_thing(self):
        info_thing = 'Название: {0}, атака: {1}, защита: {2}, жизни: {3}.'
        return info_thing.format(self.name,
                                 self.attack,
                                 self.protection,
                                 self.hp
                                 )


def install_things_player(quantity: int) -> list:
    """
    Функция возвращает сгенирированный список вещей персонажа,
    который отсортирван по проценту защиты.
    """
    things = []
    for i in range(1, quantity + 1):
        things.append(Thing(choice(THINGS)))

    things.sort(key=operator.attrgetter('protection'))

    return things