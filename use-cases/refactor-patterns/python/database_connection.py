# Database connection manager refactored with the Factory Method pattern
class DatabaseConnection:
    def __new__(cls, db_type, *args, **kwargs):
        if cls is DatabaseConnection:
            connection_class = DatabaseConnectionFactory.get_connection_class(db_type)
            return super().__new__(connection_class)

        return super().__new__(cls)

    def __init__(self, db_type, host, port, username, password, database,
                 use_ssl=False, connection_timeout=30, retry_attempts=3,
                 pool_size=5, charset='utf8'):
        self.db_type = db_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.use_ssl = use_ssl
        self.connection_timeout = connection_timeout
        self.retry_attempts = retry_attempts
        self.pool_size = pool_size
        self.charset = charset
        self.connection = None

    def connect(self):
        print(f"Connecting to {self.db_type} database...")
        self._connect()
        print("Connection successful!")
        return self.connection

    def _connect(self):
        raise ValueError(f"Unsupported database type: {self.db_type}")


class MySQLConnection(DatabaseConnection):
    def _connect(self):
        connection_string = f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        connection_string += f"?charset={self.charset}"
        connection_string += f"&connectionTimeout={self.connection_timeout}"

        if self.use_ssl:
            connection_string += "&useSSL=true"

        print(f"MySQL Connection: {connection_string}")
        # In a real app, we would: self.connection = mysql.connector.connect(...)


class PostgreSQLConnection(DatabaseConnection):
    def _connect(self):
        connection_string = f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

        if self.use_ssl:
            connection_string += "?sslmode=require"

        print(f"PostgreSQL Connection: {connection_string}")
        # In a real app, we would: self.connection = psycopg2.connect(...)


class MongoDBConnection(DatabaseConnection):
    def _connect(self):
        connection_string = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        connection_string += f"?retryAttempts={self.retry_attempts}"
        connection_string += f"&poolSize={self.pool_size}"

        if self.use_ssl:
            connection_string += "&ssl=true"

        print(f"MongoDB Connection: {connection_string}")
        # In a real app, we would: self.connection = pymongo.MongoClient(...)


class RedisConnection(DatabaseConnection):
    def _connect(self):
        print(f"Redis Connection: {self.host}:{self.port}/{self.database}")
        # In a real app, we would: self.connection = redis.Redis(...)


class DatabaseConnectionFactory:
    _connection_types = {
        'mysql': MySQLConnection,
        'postgresql': PostgreSQLConnection,
        'mongodb': MongoDBConnection,
        'redis': RedisConnection,
    }

    @classmethod
    def get_connection_class(cls, db_type):
        return cls._connection_types.get(db_type, UnsupportedDatabaseConnection)

    @classmethod
    def create_connection(cls, db_type, *args, **kwargs):
        connection_class = cls.get_connection_class(db_type)
        return connection_class(db_type, *args, **kwargs)


class UnsupportedDatabaseConnection(DatabaseConnection):
    pass


if __name__ == '__main__':
    # Example usage
    # Creating different database connections with various configurations
    mysql_db = DatabaseConnectionFactory.create_connection(
        db_type='mysql',
        host='localhost',
        port=3306,
        username='db_user',
        password='password123',
        database='app_db',
        use_ssl=True
    )
    mysql_db.connect()

    mongo_db = DatabaseConnectionFactory.create_connection(
        db_type='mongodb',
        host='mongodb.example.com',
        port=27017,
        username='mongo_user',
        password='mongo123',
        database='analytics',
        pool_size=10,
        retry_attempts=5
    )
    mongo_db.connect()
