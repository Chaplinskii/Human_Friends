import datetime

from Controller.Service.Animals.Animals import Animals
from Controller.Service.Db.Db import Db_service


class Service:
    '''Service for managing animals'''
    __id = 1

    @classmethod
    def create(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Create a new animal'''
        if id is None:
            id = cls.__id
            cls.__id += 1
        animal = Animals(id, name, date_of_birth, animal_class, species, commands)
        Db_service.add_in_db(animal)
        return print(f'Animal created successfully => {animal}')

    @classmethod
    def delete(cls, id):
        '''Delete an animal by id'''
        for i in range(0, len(cls.get_all())):
            if cls.get_all()[i].id == id:
                print(f'Animal {cls.get_all().pop(i)} deleted successfully.')
                return True
        return False

    @classmethod
    def update(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Update an animal by id'''
        for i in Service.get_all():
            if i.id == id:
                if name == None:
                    pass
                else:
                    i.name = name
                if date_of_birth == None:
                    pass
                else:
                    i.date_of_birth = date_of_birth
                if animal_class == None:
                    pass
                else:
                    i.animal_class = animal_class
                if species == None:
                    pass
                else:
                    i.species = species
                if commands == None:
                    pass
                else:
                    i.update_commands(commands)
                print(f'Animal {i} updated successfully.')
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


# print(Service.create(None,'Mike','2020-11-15',  'Mammal', 'Dog',['sit', 'run', 'jump', 'run']))
Service.create(None, 'Mike', '2020-11-15', 'Mammal', 'Dog', ['run', 'jump', 'run'])
Service.create(None, 'John', '2024-05-30', 'Pets', 'Cat', ['sit', 'run', 'run'])
Service.create(None, 'Snow', '2023-11-1', 'Pack animals', 'Horse', ['sit', 'run', 'jump', 'run'])
Service.create(None, 'Bibo', '2012-1-8', 'Pets', 'Dog', ['jump', 'run'])
# Service.create('John')

# print(Db_service.get_all())
# for i in Db_service.get_all():
#     # i.date_birthday = datetime.date(2023, 10, 8)
#     i.commands = 'sit', 'run', 'jump'
#     i.commands = 'go', 'run'
#     print(i)
