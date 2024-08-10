from Controller.Service.Service import Service


class Controller:
    '''Controller for managing animals'''

    @classmethod
    def create(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Create a new animal'''
        return Service.create(id, name, date_of_birth, animal_class, species, commands)

    @classmethod
    def delete(cls, id):
        '''Delete an animal by id'''
        return Service.delete(id)

    @classmethod
    def update(cls, id, name, date_of_birth, animal_class, species, commands):
        '''Update an animal'''
        return Service.update(id, name, date_of_birth, animal_class, species, commands)

    @classmethod
    def get_all(cls):
        '''Get all animals'''
        return Service.get_all()

    @classmethod
    def search(cls, search_type, search_input):
        '''Search for animals'''
        return Service.search(search_type, search_input)
