import psycopg2
import unittest

from models.database import Database


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.connection = psycopg2.connect(host="localhost",
                                           database="andela",
                                           user="masha",
                                           password="bhakita")
        Database.create_tables()
        self.test_user = {
            "username": "mashafrancis",
            "email": "francismasha@gmail.com",
            "password": "bhakita"
        }

    def tearDown(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users_blog')
        cursor.execute('DROP TABLE users_blog CASCADE ')
        self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    unittest.main()
