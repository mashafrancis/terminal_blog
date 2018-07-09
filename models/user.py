from models.database import Database


class UserModel:
    Database.create_tables()

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def save_to_database():
        """
        Insert a new user into the user database table
        :return:
        """
        user = (['first_name'],
                ['last_name'],
                ['username'],
                ['password'])

        sql = "INSERT INTO users_blog(user_id, first_name, last_name, username, password)" \
              "VALUES(DEFAULT, %s, %s, %s, %s)"
        
        connection = Database.dbconn()
        cursor = connection.cursor()
        cursor.execute(sql, user)

    @classmethod
    def find_by_username(cls, username):
        pass

    @classmethod
    def find_by_user_id(cls, user_id):
        pass
