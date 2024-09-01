import datetime

from Controller.Service.Animals.Animals import Animals
from Controller.Service.Db.Db import Db_service
from Controller.Service.Db.Db_SQL import Db_SQL


class Service:
    '''Service for managing animals'''
    # __id = 1
    Db_service = Db_service()
    Db_SQL = Db_SQL()

    @classmethod
    def create(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Create a new animal'''
        animal = Animals(id, name, date_of_birth, animal_class, species, commands)
        com = ", ".join(commands)
        # print(type(com))
        if id == None:
            Db_SQL.insert_animal(animal.name, date_of_birth, animal.animal_class, animal.species, com)
            Service.download_Db()
        else:
            #     id = cls.__id
            #     cls.__id += 1

            Db_service.add_in_db(animal)

        return print(f'Animal created successfully => {animal}')

    @classmethod
    def delete(cls, id):
        '''Delete an animal by id'''
        for i in range(0, len(cls.get_all())):
            if cls.get_all()[i].id == id:
                Db_SQL.delete_animal(id)
                print(f'Animal {cls.get_all().pop(i)} deleted successfully.')
                return True
        return False

    @classmethod
    def update(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Update an animal by id'''
        for i in Service.get_all():
            if i.id == id:
                if name == None:
                    name = i.name
                else:
                    i.name = name
                if date_of_birth == None:
                    date_of_birth=i.get_date()
                else:
                    i.date_of_birth = date_of_birth
                if animal_class == None:
                    animal_class = i.animal_class
                else:
                    i.animal_class = animal_class
                if species == None:
                    species = i.species
                else:
                    i.species = species
                if commands == None:
                    commands = i.update_commands
                else:
                    i.update_commands(commands)
                Db_SQL.update_animal(id, name, date_of_birth, animal_class, species, commands)
                cls.download_Db()
                print(f'Animal updated successfully.')
                return True
        return False

    @classmethod
    def get_all(cls):
        '''Get all animals'''
        return Db_service.get_all()

    @classmethod
    def search(cls, search_type, search_input):
        '''Search for animals'''
        count = 0
        for i in Db_service.get_all():
            if search_type == "name":
                if i.name.lower() == search_input.lower():
                    print(f'Result search: {i}')
                    count += 1
            if search_type == 'animal_class':
                if i.animal_class == search_input:
                    print(f'Result search: {i}')
                    count += 1
            if search_type == 'id':
                if i.id == search_input:
                    print(f'Result search: {i}')
                    count += 1
        if count == 0:
            print('No animal found.')
            return False
        else:
            print(f'Total found: {count}')
        return True

    @classmethod
    def download_Db(cls):
        '''Download database from SQL server'''
        if Service.get_all() is not None:
            Db_service.clear_db()
        rows = Db_SQL.download_database()
        for row in rows:
            cls.create(row['id'], row['name'], str(row['date_birthday']), row['class'], row['species'],
                       str(row['commands']).split(','))
