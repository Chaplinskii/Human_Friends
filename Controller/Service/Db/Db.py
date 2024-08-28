import pymysql

# from Controller.Controller_ import Controller


# from Controller.Service.Service import Service


class Db_service():
    '''Singleton class for managing the database of animals'''
    __instance = None
    __db = []
    # a= Controller.create()
    # __connection = None



    def __new__(cls, *args, **kwargs):
        # __connection = cls.connection()
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(cls):
        # cls.__connection.close()
        print('Database connection closed... bye bye! :)")')
        # cls.__connection=None
        cls.__instance = None




    @classmethod
    def add_in_db(cls, animal):
        '''Add an animal to the database'''
        cls.__db.append(animal)

    @classmethod
    def get_all(cls):
        '''Get all animals in the database'''
        return cls.__db
    @classmethod
    def clear_db(cls):
        '''Clear the database'''
        cls.__db.clear()


        # for row in cls.__connection:
        #     Controller.create(row['id'], row['name'], row['date_birthday'], row['class'], row['species'], row['commands'])

# SELECT animals.id, animals.name, animals.date_birthday, class.class, species.species, animals.commands FROM animals JOIN class ON id_class = class.id JOIN species ON id_species = species.id;
