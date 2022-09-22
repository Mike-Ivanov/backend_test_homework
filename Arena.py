
from Person import get_list_players, print_persons
from Thing import install_things_player

from random import randint

if __name__ == '__main__':
    persons = get_list_players()

    for i in range(1, len(persons)):
        persons[i].set_things(install_things_player(randint(1, 5)))

    print_persons(persons)

    round = 1

    while len(persons) > 1:
        print(f'\n************* Раунд № {round} ************')
        len_before_round = len(persons)
        persons_after_round = []

        for i in range(0, int(len_before_round / 2)):
            if len(persons) == 1:
                break
            attacker = persons.pop(randint(0, len(persons) - 1))
            defender = persons.pop(randint(0, len(persons) - 1))
            defender.get_damage(attacker)
            persons_after_round.append(attacker)
            if defender.is_a_life:
                persons_after_round.append(defender)

        persons = persons_after_round
        round += 1

    print('\nПобедитель: ' + persons[0].get_player())