import datetime
from string import ascii_letters


class Verification_menu:

    @classmethod
    def verify_input_menu(cls, choice, value):
        '''Verify if the input is a valid menu choice. 0 is the exit option.'''
        if choice not in value:
            print(f'Invalid input: {choice}')
            return True
        return False


class Verification_create():
    '''Class for validating input during creating a new animal'''
    letter_rus = 'йцукенгшщзхъэждлорпавыфячсмитьбю-'
    letter_rus_Upper = letter_rus.upper()
    letter = ascii_letters + letter_rus + letter_rus_Upper
    list_animal_classes = {1: 'Pets', 2: 'Pack animals'}
    keys_list = list(list_animal_classes.keys())
    list_pets_species = {1: 'Dog', 2: 'Cat', 3: 'Hamster'}
    keys_list_pets_species = list(list_pets_species.keys())
    list_pack_animals_species = {1: 'Horse', 2: 'Camel', 3: 'Donkey'}
    keys_list_pack_animals_species = list(list_pack_animals_species.keys())

    @classmethod
    def verify_name(cls, name):
        '''Verify if the name is valid.'''
        if type(name) is not str:
            raise ValueError('Name must be a string.')
        if len(name) < 1:
            raise ValueError('Name must not be empty.')
        if len(name.strip(cls.letter)) != 0:
            raise ValueError('Name must contain only latin letters and cyrillic letters.')

    @classmethod
    def verify_date_of_birth(cls, date_of_birth):
        '''Verify if the date of birth is valid.'''
        f = date_of_birth.split('-')
        if len(f) != 3:
            raise ValueError('Date of birth must be in format YYYY-MM-DD.')
        if len(f[0]) != 4 or len(f[1]) != 2 or len(f[2]) != 2:
            raise ValueError('Date of birth must be in format YYYY-MM-DD.')

        try:
            d = datetime.datetime(int(f[0]), int(f[1]), int(f[2]))
            if d > datetime.datetime.now():
                raise ValueError('Date of birth must be a past date.')
        except ValueError:
            raise ValueError('Date of birth must be a valid date.')

    @classmethod
    def verify_animal_class(cls, animal_class):
        if animal_class not in cls.keys_list:
            raise ValueError('Invalid animal class.')

    @classmethod
    def verify_species(cls, species, animal_class):
        '''Verify if the species is valid.'''
        if animal_class == 1:
            if species not in cls.keys_list_pets_species:
                raise ValueError('Invalid pet species.')
        if animal_class == 2:
            if species not in cls.keys_list_pack_animals_species:
                raise ValueError('Invalid pack animal species.')

    @classmethod
    def verify_commands(cls, commands):
        '''Verify if the commands are valid.'''
        if type(commands) is not str:
            raise ValueError('Name must be a string.')
        if len(commands.strip(cls.letter)) != 0:
            raise ValueError('Name must contain only latin letters and cyrillic letters.')

