from dataclasses import dataclass
from operator import attrgetter
from ../venv/lib/site-packages/colorama import Fore, Style
import random
from typing import List


@dataclass
class Thing:
    """Класс предметов персонажей."""
    name: str
    percent_of_protection: float
    damage: float
    hit_points: float


@dataclass
class Person:
    """Базовый класс персонажей."""
    name: str
    hit_points: float
    base_attack: float
    base_defence: float
    things: list = None
    magic_power: float = 0

    def set_things(self, things: List[Thing]) -> None:
        """Передать распределенные предметы персонажу."""
        self.things = things

    def get_damage(self, damge: float) -> None:
        """Получить повреждение во время битвы."""
        final_protection = self.get_final_protection()
        self.hit_points = self.hit_points - (damge - damge * final_protection)

    def get_final_protection(self) -> float:
        """Получить общий коэффициент защиты от предметов."""
        final_protection = 0
        for item in self.things:
            final_protection += item.percent_of_protection

        final_protection = (final_protection + self.base_defence)/100

        return final_protection

    def get_waepon_damage(self) -> float:
        """Получить силу оружия."""
        weapon_damage = 0
        for item in self.things:
            weapon_damage += item.damage

        return weapon_damage


class Paladin(Person):
    """Специализация персонажа: паладин."""
    def __init__(self, name, hit_points, base_attack, base_defence) -> None:
        super().__init__(name, hit_points, base_attack, base_defence)

        self.hit_points = 2 * hit_points
        self.base_defence = 2 * base_defence


class Warrior(Person):
    """Специализация персонажа: воин."""
    def __init__(self, name, hit_points, base_attack, base_defence) -> None:
        super().__init__(name, hit_points, base_attack, base_defence)

        self.base_attack = 2 * base_attack


class Mage(Person):
    """Специализация персонажа: воин."""
    def __init__(self, name, hit_points, base_attack, base_defence) -> None:
        super().__init__(name, hit_points, base_attack, base_defence)

        self.magic_power = 100


def create_items() -> List[Thing]:
    """Генерация начального списка игровых предметов"""
    items = []
    weapon_names = ['sword', 'falchion', 'glaive', 'dagger', 'knife', 'cudgel', 'mace', 'axe', 'bow', 'staff']
    armor_name = ['helmet', 'bracers', 'chest', 'boots', 'cape', 'shield',
                  'trousers', 'gloves', 'ring of protection', 'glasses']

    i = 0
    while i <= 9:
        items.append(Thing(weapon_names[i], 0, random.randrange(0, 150, 1), random.randrange(0, 10, 1)))
        i += 1

    i = 0
    while i <= 9:
        items.append(Thing(armor_name[i], random.randrange(0, 10, 1), 0, random.randrange(0, 10, 1)))
        i += 1
    items = sorted(items, key=attrgetter('percent_of_protection'))
    return items


def create_characters(number_characters: int) -> list:
    """Генерация персонажий"""
    characters = []
    names = ['Frodo Baggins', 'Gandalf the Grey', 'Samwise Gamgee', 'Meriadoc Brandybuck', 'Peregrin Took', 'Aragorn',
             'Legolas', 'Gimli', 'Boromir', 'Sauron', 'Gollum', 'Bilbo Baggins', 'Tom Bombadil', 'Elrond',
             'Arwen Evenstar', 'Galadriel', 'Saruman the White', 'Eomer', 'Theoden', 'Eowyn']

    i = 0
    while i <= number_characters:
        choice = random.choice([1, 2, 3])
        if choice == 1:
            characters.append(Paladin(names[i], 100, 10, 5))
        elif choice == 2:
            characters.append(Warrior(names[i], 100, 10, 5))
        else:
            characters.append(Mage(names[i], 50, 10, 5))
        i += 1

    return characters


def make_battle_action(side1, side2) -> None:
    """Атака"""
    attack_power = side1.base_attack + side1.get_waepon_damage() + side1.magic_power
    damage = attack_power - attack_power * side2.get_final_protection()
    battle_msg = (f'{type(side1).__name__} {side1.name} наносит удар по {type(side2).__name__} '
                  f'{side2.name} на {Fore.MAGENTA} {str(damage)} {Style.RESET_ALL} урона')
    side2.get_damage(attack_power)
    print(battle_msg)


def make_things_older(list_of_thing_lists: List[list]) -> None:
    """Износ предметов"""
    for thing_list in list_of_thing_lists:
        for item in thing_list:
            item.hit_points = item.hit_points - item.hit_points * 0.40
            if item.hit_points <= 0:
                print(f'Предмет {Fore.LIGHTYELLOW_EX} {item.name} {Style.RESET_ALL} не выдержал натиска времени')
                thing_list.remove(item)


def main(number_characters) -> None:
    characters = create_characters(number_characters)
    items = create_items()

    for character in characters:
        quantity_of_items = random.randrange(1, 4, 1)
        items_set = []
        i = 0
        while i <= (quantity_of_items-1):
            item_number = random.randrange(0, 20, 1)
            items_set.append(items[item_number])
            i += 1

        character.set_things(items_set)
    i = 0
    while not len(characters) == 1:
        # Определяем бойцов и кто будет ходить первым случайным образом
        if len(characters) == 2:
            attacker = characters[0]
            defender = characters[1]
        else:
            attacker = characters[random.randrange(0, (number_of_characters-i), 1)]
            defender = characters[random.randrange(0, (number_of_characters-i), 1)]
        turn = 1

        # Сражение происходит до того пока у кого то из соперников не кончится жизнь
        while attacker.hit_points > 0 and defender.hit_points > 0 and (not attacker == defender):
            if turn % 2 != 0:
                make_battle_action(attacker, defender)
            else:
                make_battle_action(defender, attacker)
            turn += 1

        # Все вещи участников изнашиваются после боя на 10%. Сломанные вещи удаляются из инвентаря
        make_things_older([attacker.things, defender.things])

        # Проигравший удаляется с арены. Проигравший получает его вещи
        if attacker.hit_points < 0 and turn > 1:
            print(f'{Fore.RED} {attacker.name} погибает {Style.RESET_ALL}')
            for item in attacker.things:
                defender.things.append(item)
            characters.remove(attacker)
            i += 1
        elif defender.hit_points < 0 and turn > 1:
            print(f'{Fore.RED} {defender.name} погибает {Style.RESET_ALL}')
            for item in defender.things:
                attacker.things.append(item)
            characters.remove(defender)
            i += 1
        else:
            pass

    print(f'{Fore.GREEN} {characters[0].name} пбеждает {Style.RESET_ALL}')


if __name__ == '__main__':
    number_of_characters_str = input('Введите количество персонажей (не больше 20): ')

    try:
        number_of_characters = int(number_of_characters_str)

        if number_of_characters <= 20:
            main(number_of_characters)
        else:
            print('Введено не корректное значение')
    except IndexError:
        print('Введено не корректное значение')
        raise