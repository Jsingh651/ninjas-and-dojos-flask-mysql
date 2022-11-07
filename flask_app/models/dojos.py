import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def get_all (cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        dojos = []
        for i in results:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def save (cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)

    @classmethod
    def getone(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s"
        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)

    @classmethod
    def get_dojo_with_ninjas(cls ,data):
        query = """
                SELECT * FROM dojos LEFT JOIN ninjas
                ON ninjas.dojos_id = dojos.id    
                WHERE dojos.id = %(id)s;

                """
                # table 1 JOIN table 2 ON primary key = foreign key
                # ninjas.dojos_id = foreign key
                #  dojos.id = primary key
                # LEFT JOIN means 
                # dojos table (on the left) shows every row
                # ninjas table (on the right) only shows rows that have a match on the left

        results = connectToMySQL('dojos_ninjas_schemca').query_db( query , data)
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojos_id": row_from_db['dojos_id']
            }
            dojo.ninjas.append( ninjas.Ninja( ninja_data ))
        return dojo



