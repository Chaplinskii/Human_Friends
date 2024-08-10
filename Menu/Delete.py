from Menu.Search import Search
from Controller.Controller import Controller
from Menu.Verification import Verification_menu


class Delete:
    '''Delete an animal'''

    @classmethod
    def delete(cls):
        '''Delete an animal'''
        result = Delete.enter_id()
        if result == -1:
            return True
        if Controller.delete(result) == False:
            print('Animal not found.')
            return Delete.delete()
        return True

    @classmethod
    def enter_id(cls):
        try:
            print('Enter the id of the animal you want to delete:')
            id = int(input('0.Exit  Enter the id of the animal: '))
            if id < 0:
                raise ValueError('ID must be a positive integer')
            if id == 0:
                return -1
        except ValueError as e:
            print(f'Invalid input. Please enter a valid id. {e}')
            return Delete.enter_id()  # recursion until valid input is provided
        return id
