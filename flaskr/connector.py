import os
import sys
import psycopg2

from dotenv import load_dotenv

load_dotenv()


class Connector:
    def __init__(self, host_name: str, db_name: str, port_number: int):
        # Get username and password from environment variables
        user_name = os.getenv('POSTGRES_USER')
        password = os.getenv('POSTGRES_PASSWORD')
        try:
            # Establish connection with postgres server
            self.connection = psycopg2.connect(host=host_name, dbname=db_name, user=user_name,
                                               password=password, port=port_number)
            # Create a cursor
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1)

    def test_connection(self):
        print('Connection to database successful.')
        self.cursor.execute('SELECT version()')
        db_version = self.cursor.fetchone()
        print(db_version)
        self.cursor.close()
