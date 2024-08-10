import os


class Exit:
    '''Exit the program class.'''
    @staticmethod
    def exit():
        '''Exit the program.'''
        print('Exiting...')
        os._exit(0)
