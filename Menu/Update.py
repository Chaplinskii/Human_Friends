from Controller.Controller import Controller
from Menu.Create import Create
from Menu.Verification import Verification_create
import datetime


class Update(Create, Verification_create):
    '''Update an animal class'''
    __list_of_animals = Controller.get_all()
    __spec = None

    @classmethod
    def update(cls):
        '''Update an animal class'''
        __id = Update.enter_id()
        if __id == -1:
            return -1
        if Update.checking_for_id_availability(__id) == -2:
            print('No animals found.')
            return Update.update()
        else:
            id = __id
            name = Update.enter_name()
            birth_date = Update.enter_date_of_birth()
            animal_class = Update.enter_animal_class()
            species = Update.enter_species()
            commands = Update.enter_commands()
            Controller.update(id, name, birth_date, animal_class, species, commands)
        return -1

    @classmethod
    def enter_id(cls):
        try:
            print('Enter the id of the animal you want to update:')
            id = int(input('0.Exit  Enter the id of the animal: '))
            if id < 0:
                raise ValueError('ID must be a positive integer')
            if id == 0:
                return -1
        except ValueError as e:
            print(f'Invalid input. Please enter a valid id. {e}')
            return Update.enter_id()  # recursion until valid input is provided
        return id

    @classmethod
    def checking_for_id_availability(cls, id):
        '''Check if id is available'''

        for animal in cls.__list_of_animals:
            if animal.id == id:
                print(f'Animal with id {id} already exists.')
                return True
        return -2

    @classmethod
    def enter_name(cls):
        try:
            name = input('0.Exit  Enter the name of the animal: ')
            if name == '0':
                return False
            if name == "":
                return None
            Update.verify_name(name)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid name. {e}')
            return Update.enter_name()  # recursion until valid input is provided
        return name

    @classmethod
    def enter_date_of_birth(cls):
        try:
            date_of_birth = input('0.Exit  Enter the date of birth (YYYY-MM-DD): ')
            if date_of_birth == "":
                return None
            if date_of_birth == '0':
                return False
            if date_of_birth != None:
                Update.verify_date_of_birth(date_of_birth)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid date of birth. {e}')
            return Update.enter_date_of_birth()  # recursion until valid input is provided
        return date_of_birth

    @classmethod
    def enter_animal_class(cls):
        try:
            print(f'Available animal classes: ')
            for i in Update.keys_list:
                print(f'{i} : {Update.list_animal_classes.get(i)}')
            animal_class = input('0.Exit  Enter the animal class: ')
            if animal_class == "":
                return None
            animal_class=int(animal_class)
            if animal_class == 0:
                return False
            Update.verify_animal_class(animal_class)
            cls.__spec = animal_class
        except ValueError as e:
            print(f'Invalid input. Please enter a valid animal class. {e}')
            return Update.enter_animal_class()  # recursion until valid input is provided
        return Update.list_animal_classes.get(animal_class)

    @classmethod
    def enter_species(cls):
        try:
            if Update.__spec == None:
                return None
            if Update.__spec == 1:
                print(f'Available pets species: ')
                for i in Update.keys_list_pets_species:
                    print(f'{i} : {Update.list_pets_species.get(i)}')
                species = int(input('0.Exit  Enter the species: '))
                if species == 0:
                    return False
                Update.verify_species(species, Update.__spec)
                return Update.list_pets_species.get(species)
            if Update.__spec == 2:
                print(f'Available pack animals species: ')
                for i in Update.keys_list_pack_animals_species:
                    print(f'{i} : {Update.list_pack_animals_species.get(i)}')
                species = int(input('0.Exit  Enter the species: '))
                if species == 0:
                    return False
                Update.verify_species(species, Update.__spec)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid species. {e}')
            return Update.enter_species()  # recursion until valid input is provided

    @classmethod
    def enter_commands(cls):
        err = None
        try:
            commands = input('0.Exit  Enter commands (separated by commas \",\"): ').split(',')
            if "0" in commands:
                return False
            if commands == []:
                return commands
            if len(commands) != 0:
                for i in commands:
                    err = i
                    Update.verify_commands(i)
        except ValueError as e:
            print(f'Invalid input: >{err}< . Please enter a valid command. {e}')
            return Update.enter_commands()  # recursion until valid input is provided
        return set(commands)

    @classmethod
    def verify_name(cls, name):
        if type(name) is not str:
            raise ValueError('Name must be a string.')
        if len(name.strip(cls.letter)) != 0:
            raise ValueError('Name must contain only latin letters and cyrillic letters.')

    @classmethod
    def verify_date_of_birth(cls, date_of_birth):
        return super().verify_date_of_birth(date_of_birth)

    @classmethod
    def verify_animal_class(cls, animal_class):
        return super().verify_animal_class(animal_class)

    @classmethod
    def verify_species(cls, species, animal_class):
        return super().verify_species(species, animal_class)

    @classmethod
    def verify_commands(cls, commands):
        return super().verify_commands(commands)
