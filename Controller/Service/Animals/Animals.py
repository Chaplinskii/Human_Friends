import datetime


class Animals:
    '''Represents an animal'''

    __id = int()
    __name = str()
    __date_birthday = datetime
    __commands = []
    __animal_class = str()
    __species = str()

    def get_id(self):
        '''Get the unique identifier of the animal'''
        return self.__id

    def set_id(self, id):
        '''Set the unique identifier of the animal'''
        if id is None:
            self.__id = None
        elif id < 0:
            raise ValueError('ID must be a non-negative integer')
        else:
            self.__id = id

    id = property(get_id, set_id)

    def get_name(self):
        '''Get the name of the animal'''
        return self.__name

    def set_name(self, name):
        '''Set the name of the animal'''
        self.__name = name

    name = property(get_name, set_name)

    def get_date_birthday(self):
        '''Get the age of the animal'''
        if self.__date_birthday != None:
            year = datetime.date.today().year - self.__date_birthday.year
            month = datetime.date.today().month - self.__date_birthday.month
            if month < 0:
                if month < 0 and year == 1:
                    year = 0
                month += 12
            day = datetime.date.today().day - self.__date_birthday.day
            if day < 0:
                day += 30
            return f' {year}-Year, {month}-month, {day}-day'
        else:
            return self.__date_birthday

    def set_date_birthday(self, date):
        '''Set the date of birth of the animal'''
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if date > date.today():
                raise ValueError('Date mast be a past date')
        except Exception as e:
            print(f'Error: {e}')
        else:
            self.__date_birthday = date

    date_birthday = property(get_date_birthday, set_date_birthday)

    def get_commands(self):
        '''Get the commands of the animal'''
        return self.__commands

    def set_commands(self, args):
        '''Set the commands of the animal'''
        self.__commands = set(args)

    commands = property(get_commands, set_commands)

    def get_animal_class(self):
        '''Get the class of the animal'''
        return self.__animal_class

    def set_animal_class(self, animal_class):
        '''Set the class of the animal'''
        self.__animal_class = animal_class

    animal_class = property(get_animal_class, set_animal_class)

    def get_species(self):
        '''Get the species of the animal'''
        return self.__species

    def set_species(self, species):
        '''Set the species of the animal'''
        self.__species = species

    species = property(get_species, set_species)

    def update_commands(self, commands):
        '''Update the commands of the animal'''
        self.__commands.update(commands)

    def __init__(self, id, name, date, animal_class, species, commands):
        self.id = id
        self.name = name
        self.date_birthday = date
        self.commands = commands
        self.animal_class = animal_class
        self.species = species

    def __str__(self):
        '''String representation of the Animal object.'''
        return f'ID: {self.get_id()}, Name: {self.get_name()}, Age: {self.get_date_birthday()}, Class: {self.get_animal_class()}, Species: {self.get_species()}, Commands: {self.get_commands()}'
