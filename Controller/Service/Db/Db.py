class Db_service:
    '''Singleton class for managing the database of animals'''
    __instance = None
    __db = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(cls):
        cls.__instance = None

    @classmethod
    def add_in_db(cls, animal):
        '''Add an animal to the database'''
        cls.__db.append(animal)

    @classmethod
    def get_all(cls):
        '''Get all animals in the database'''
        return cls.__db
