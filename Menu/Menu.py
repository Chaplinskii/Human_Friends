from Menu.Exit import Exit
from Menu.Verification import Verification_menu
from Menu.Create import Create
from Menu.Get_all import Get_all
from Menu.Search import Search
from Menu.Delete import Delete
from Menu.Update import Update


class Menu:
    ''' Menu'''

    @classmethod
    def menu(cls):
        ''' Menu constructor'''
        __list_menu = [1,2,3,4,5,0]
        print('MENU:  1.Create an animal  2.Delete an animal  3.Update an animal  4.Get all animals  5.Search  0.Exit')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError as e:
            print(f'Invalid input. Please enter a number. {e}')
            return Menu.menu()
        if Verification_menu.verify_input_menu(choice, __list_menu):
            return Menu.menu()
        if choice == 0:
            Exit.exit()
        if choice == 1:
            if Create.create():
                return Menu.menu()
        if choice == 2:
            if Delete.delete():
                return Menu.menu()
        if choice == 3:
            if Update.update()==-1:
                return Menu.menu()
        if choice == 4:
            if Get_all.get_all():
                return Menu.menu()
        if choice == 5:
            if Search.search():
                return Menu.menu()
