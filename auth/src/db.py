import psycopg
from psycopg_pool import ConnectionPool

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection_pool = None

    def initialize_pool(self):
        self.connection_pool = ConnectionPool(
            user=self.db_config['user'],
            password=self.db_config['password'],
            host=self.db_config['host'],
            port=self.db_config['port'],
            database=self.db_config['database']
        )

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

# Example usage
if __name__ == "__main__":
    db_config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432',
        'database': 'your_database'
    }

    db = Database(db_config)
    db.initialize_pool()

    # Use the connection with a context manager
    with db.connection() as conn:
        # Use the connection
        # ...

    # Close all connections when done
    db.close_all_connections()