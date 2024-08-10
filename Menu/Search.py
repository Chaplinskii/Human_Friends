from Menu.Verification import *
from Controller.Controller import Controller


class Search:
    '''Class for searching animals'''
    __list_menu = [1, 2, 3, 0]

    @classmethod
    def search(cls):
        '''Search for animals'''

        print('Search for animals: 1. Name  2. Class  3. ID  0. Exit')
        try:
            search_type = int(input('Enter your choice: '))
            if Verification_menu.verify_input_menu(search_type, cls.__list_menu):
                raise ValueError()
            if search_type == 1:
                return cls.search_by_name()
            if search_type == 2:
                return cls.search_by_class()
            if search_type == 3:
                return cls.search_by_id()
            if search_type == 0:
                return True
        except ValueError as e:
            print(f'Invalid input. Please enter a number. {e}')
            return cls.search()
        return True

    @classmethod
    def search_by_name(cls):
        '''Search for animals by name'''
        search_type = 'name'
        try:
            search_input = input('0.Exit  Enter the name of the animal: ')
            if search_input == '0':
                return cls.search()
            Verification_create.verify_name(search_input)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid name. {e}')
            return cls.search_by_name()
        return Controller.search(search_type, search_input)

    @classmethod
    def search_by_id(cls):
        '''Search for animals by id'''
        search_type = 'id'
        try:
            search_input = int(input('0.Exit  Enter the id of the animal: '))
            if search_input <0:
                raise ValueError('ID must be a positive integer')
            if search_input == 0:
                return cls.search()

        except ValueError as e:
            print(f'Invalid input. Please enter a valid id. {e}')
            return cls.search_by_id()
        return Controller.search(search_type, search_input)

    @classmethod
    def search_by_class(cls):
        '''Search for animals by class'''
        search_type = "animal_class"
        try:
            print(f'Available animal classes: ')
            for i in Verification_create.keys_list:
                print(f'{i} : {Verification_create.list_animal_classes.get(i)}')
            animal_class = int(input('0.Exit  Enter the animal class: '))
            if animal_class == 0:
                return cls.search()
            Verification_create.verify_animal_class(animal_class)
        except ValueError as e:
            print(f'Invalid input. Please enter a valid class. {e}')
            return cls.search_by_class()
        return Controller.search(search_type, Verification_create.list_animal_classes.get(animal_class))
