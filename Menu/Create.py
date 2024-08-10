from Controller.Controller import Controller
from Menu.Verification import Verification_create



class Create:
    '''Class for creating a new animal'''
    __spec = None
    @classmethod
    def create(cls):
        '''Create a new animal'''
        id = None
        name = Create.enter_name()
        if name == False:
            return True
        date_of_birth = Create.enter_date_of_birth()
        if date_of_birth == False:
            return True
        animal_class = Create.enter_animal_class()
        if animal_class == False:
            return True
        species = Create.enter_species()
        if species == False:
            return True
        commands = Create.enter_commands()
        if commands == False:
            return True
        Controller.create(id, name, date_of_birth, animal_class, species, commands)
        return True

    @classmethod
    def enter_name(cls):
        '''Enter the name of the animal'''
        try:
            name = input('0.Exit  Enter the name of the animal: ')
            if name == '0':
                return False
            Verification_create.verify_name(name)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid name. {e}')
            return Create.enter_name()  # recursion until valid input is provided
        return name

    @classmethod
    def enter_date_of_birth(cls):
        '''Enter the date of birth of the animal'''
        try:
            date_of_birth = input('0.Exit  Enter the date of birth (YYYY-MM-DD): ')
            if date_of_birth == '0':
                return False
            Verification_create.verify_date_of_birth(date_of_birth)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid date of birth. {e}')
            return Create.enter_date_of_birth()  # recursion until valid input is provided
        return date_of_birth

    @classmethod
    def enter_animal_class(cls):
        '''Enter the animal class'''
        try:
            print(f'Available animal classes: ')
            for i in Verification_create.keys_list:
                print(f'{i} : {Verification_create.list_animal_classes.get(i)}')
            animal_class = int(input('0.Exit  Enter the animal class: '))
            if animal_class == 0:
                return False
            Verification_create.verify_animal_class(animal_class)
            cls.__spec = animal_class
        except ValueError as e:
            print(f'Invalid input. Please enter a valid animal class. {e}')
            return Create.enter_animal_class()  # recursion until valid input is provided
        return Verification_create.list_animal_classes.get(animal_class)

    @classmethod
    def enter_species(cls):
        '''Enter the species of the animal'''
        try:
            if Create.__spec == 1:
                print(f'Available pets species: ')
                for i in Verification_create.keys_list_pets_species:
                    print(f'{i} : {Verification_create.list_pets_species.get(i)}')
                species = int(input('0.Exit  Enter the species: '))
                if species == 0:
                    return False
                Verification_create.verify_species(species, Create.__spec)
                return Verification_create.list_pets_species.get(species)
            if Create.__spec == 2:
                print(f'Available pack animals species: ')
                for i in Verification_create.keys_list_pack_animals_species:
                    print(f'{i} : {Verification_create.list_pack_animals_species.get(i)}')
                species = int(input('0.Exit  Enter the species: '))
                if species == 0:
                    return False
                Verification_create.verify_species(species, Create.__spec)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid species. {e}')
            return Create.enter_species()  # recursion until valid input is provided


    @classmethod
    def enter_commands(cls):
        '''Enter the commands of the animal'''
        err = None
        try:
            commands = input('0.Exit  Enter commands (separated by commas \",\"): ').split(',')
            if "0" in commands:
                return False
            if len(commands)!=0:
                for i in commands:
                    err = i
                    Verification_create.verify_commands(i)
        except ValueError as e:
            print(f'Invalid input: >{err}< . Please enter a valid command. {e}')
            return Create.enter_commands()  # recursion until valid input is provided
        return commands