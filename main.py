from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон равный {5 + randint(-3, -1)}')
    else:
        return (f'{char_name} не применил атаку')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    else:
        return (f'{char_name} не применил защиту')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} применил умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил умение «Защита {10 + 30}»')
    else:
        return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи 1 из команд: attack, defence, special.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи класс персонажа: warrior, mage, healer.')
        if char_class == 'warrior':
            print('Warior — воин ближнего боя.')
        if char_class == 'mage':
            print('Mage — воитель дальнего боя. Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Healer — цилитель, черпает силы из природы, веры и духов.')
        approve_choice = input('Y- подтвердить, T- сменить персонажа.').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ') 
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
