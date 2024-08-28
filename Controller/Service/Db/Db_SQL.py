from datetime import datetime

import pymysql


class Db_SQL:
    '''Class for database SQL queries'''

    __instance = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(cls):
        if cls.__connection is not None:
            cls.__connection.close()
        cls.__instance = None

    def connection(self):
        '''Database connection'''
        try:
            self.__connection = pymysql.connect(
                host='127.0.0.1',
                port=3331,
                # user='user_human_friends',
                user='hacoc',
                # user='root',
                password='123',
                database='Human_Friends',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            print("#" * 20)
            return self.__connection
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def close_connection(self):
        if self.__connection is not None:
            self.__connection.close()
        Db_SQL.__connection = None
        print('Database connection closed... bye bye! :)')

    @classmethod
    def download_database(cls):
        '''Download database from SQL server'''
        cls.__connection = cls.connection(cls.__instance)
        try:
            with cls.__connection.cursor() as cursor:
                # select_all_rows = "SELECT animals.id, animals.name, animals.date_birthday, class.class, species.species, animals.commands FROM animals JOIN class ON id_class = class.id JOIN species ON id_species = species.id;"
                select_all_rows = "CALL `proc_get_all`(@p0);"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print('Error occurred while getting data from the database:', ex)
        finally:
            cls.close_connection(cls.__instance)

    @classmethod
    def insert_animal(cls, name, date_birthday, class_id, species_id, commands):
        '''Insert new animal into the database'''
        cls.__connection = cls.connection(cls.__instance)
        try:
            with cls.__connection.cursor() as cursor:
                # insert_animal_query = "INSERT INTO animals SET name = \""+str(name)+"\", date_birthday = \""+str(date_birthday)+"\", id_class = (SELECT class.id FROM class WHERE class = \""+str(class_id)+"\"), id_species = (SELECT species.id FROM species WHERE species = \""+str(species_id)+"\"), commands = \""+commands+"\""
                insert_animal_query = "CALL `proc_insert`(@sp0,\"" + str(name) + "\", \"" + str(
                    date_birthday) + "\", \"" + str(class_id) + "\", \"" + str(species_id) + "\", \"" + str(
                    commands) + "\");"
                print(insert_animal_query)
                cursor.execute(insert_animal_query)
                cls.__connection.commit()
                print("Animal added successfully.")
        except Exception as ex:
            print('Error occurred while inserting data into the database:', ex)
        finally:
            cls.close_connection(cls.__instance)

    @classmethod
    def delete_animal(cls, id):
        '''Delete an animal from the database by id'''
        cls.__connection = cls.connection(cls.__instance)
        try:
            with cls.__connection.cursor() as cursor:
                # delete_animal_query = "DELETE FROM animals WHERE id = "+str(id)
                delete_animal_query = "CALL `proc_delete`(@p0, \"" + str(id) + "\");"
                cursor.execute(delete_animal_query)
                cls.__connection.commit()
                print("Animal deleted successfully.")
        except Exception as ex:
            print('Error occurred while deleting data from the database:', ex)
        finally:
            cls.close_connection(cls.__instance)

    @classmethod
    def update_animal(cls, id, name, date_birthday, class_id, species_id, commands):
        '''Update an animal in the database'''
        cls.__connection = cls.connection(cls.__instance)
        try:
            with cls.__connection.cursor() as cursor:
                # update_animal_query = "UPDATE animals SET name = \""+str(name)+"\", date_birthday = \""+str(date_birthday)+"\", id_class = (SELECT class.id FROM class WHERE class = \""+str(class_id)+"\"), id_species = (SELECT species.id FROM species WHERE species = \""+str(species_id)+"\"), commands = \""+commands+"\" WHERE id = "+str(id)
                update_animal_query = "CALL `proc_update`(@sp0,\"" + str(id) + "\",\"" + str(name).capitalize() + "\", \"" + str(
                    date_birthday) + "\", \"" + str(class_id) + "\", \"" + str(species_id) + "\", \"" + str(
                    commands).strip('{} \'\"') + "\");"
                cursor.execute(update_animal_query)
                cls.__connection.commit()
                print("Animal updated successfully.")
        except Exception as ex:
            print('Error occurred while updating data from the database:', ex)
        finally:
            cls.close_connection(cls.__instance)
