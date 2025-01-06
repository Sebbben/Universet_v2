import psycopg
from psycopg_pool import ConnectionPool
import os

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection_pool = None

    def initialize_pool(self):
        self.connection_pool = ConnectionPool({
            "user": self.db_config['user'],
            "password": self.db_config['password'],
            "host": self.db_config['host'],
            "port": self.db_config['port'],
            "database": self.db_config['database']
        })

    def get_connection(self):
        if not self.connection_pool:
            self.initialize_pool()
        return self.connection_pool.getconn()

    def release_connection(self, connection):
        if self.connection_pool:
            self.connection_pool.putconn(connection)

    def close_all_connections(self):
        if self.connection_pool:
            self.connection_pool.closeall()

    class ConnectionContext:
        def __init__(self, db_instance):
            self.db_instance = db_instance
            self.conn = None

        def __enter__(self):
            self.conn = self.db_instance.get_connection()
            return self.conn

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.db_instance.release_connection(self.conn)

    def connection(self):
        return self.ConnectionContext(self)


DB = None
# Example usage
def init():

    db_config = {
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("DATABASE_HOST"),
        'port': os.getenv("DATABASE_PORT"),
        'database': os.getenv("POSTGRES_DB")
    }

    DB = Database(db_config)
    DB.initialize_pool()
