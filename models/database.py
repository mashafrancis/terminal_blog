import psycopg2


class Database:
    @staticmethod
    def dbconn():
        connection = psycopg2.connect(dbname='andela',
                                      host='localhost',
                                      user='masha',
                                      password='bhakita')
        return connection

    @staticmethod
    def create_tables():
        """
        Create tables for users
        :return:
        """
        command = (
            """
            CREATE TABLE users_blog (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR (80) NOT NULL,
                email VARCHAR (80) NOT NULL,
                password VARCHAR (80) NOT NULL
                )
            """
        )
        connection = None
        try:
            connection = Database.dbconn()
            cursor = connection.cursor()
            cursor.execute(command)
            cursor.close()
            cursor.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()


if __name__ == '__main__':
    Database.create_tables()
