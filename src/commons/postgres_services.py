import psycopg2


class PostgresClients:
    """NoodleMongoClient."""

    def __init__(self):
        """Init.

        method is run as soon as an object of a class is instantiated.
        The method is useful to do any initialization you want to do
        with your object
        """
        self.client =  psycopg2.connect(database="postgres", user = "postgres", password = "prajwal.wale", host = "127.0.0.1")


