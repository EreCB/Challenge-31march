import P3_SmA_animals

menu = {
    '1': '1. Eagle 🦅',
    '2': '2. Owl 🦉',
    '3': '3. Dolphin 🐬',
    '4': '4. Wolf 🐺',
    '5': '5. Fish 🐠',
    '6': '6. Exit game 🌺'
}

class Animal():
    def __init__(self, type):
        self.type = type
        
    def show_animal(self):
        animal_art = getattr(P3_SmA_animals, self.type)
        return animal_art

# Ejecución principal
if __name__ == '__main__':

    print('================================================================================')
    print('================================================================================')
    print('                             SHOW ME AN ANIMAL \n')
    print('                             Welcome to the game\n')
    print('From the menu below, please choose the animal you want to print:\n')
    
    for option in menu:
        print(menu.get(option))

    while True:
        choice = input('\nChoose your animal or exit the game: --> ')

        if choice == '6':
            print('\nEnd of the game. Thanks for playing. We hope to see you again soon!\n')
            print('================================================================================')
            break

        elif choice in menu:
            menu_value = menu.get(choice)
            animal_type = menu_value.split()[1]
            my_animal = Animal(animal_type)
            final_print = my_animal.show_animal()
            print(final_print)

        else:
            print('\nYour choice is incorrect. Choose again.\n')