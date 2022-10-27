from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def get_all_ninjas(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        ninjas = []
        for i in results:
            ninjas.append(cls(i))
        return ninjas

    @classmethod
    def save_ninjas(cls,data):
        query = '''INSERT INTO ninjas 
        (first_name, last_name, age, dojos_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojos_id)s);'''

        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)

    @classmethod
    def delete_ninja(cls,data):
        query = 'DELETE FROM ninjas WHERE ninjas.id = (%(id)s);'
        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)

    @classmethod
    def getone(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = """
        UPDATE ninjas SET 
        first_name = %(first_name)s, 
        last_name = %(last_name)s, 
        age = %(age)s
        WHERE id = %(ninja_id)s; 
        """
        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)
