# ------------------------------------------------------------------------------
# CUSTOM FUNCTION IMPORTS
# ------------------------------------------------------------------------------
import psycopg2

# ------------------------------------------------------------------------------
# PYMONGO FEATURES IMPORT
# ------------------------------------------------------------------------------

from commons.json_utils import to_json, to_list_json
from commons.postgres_services import PostgresClients


class BankService:
    """Login Service"""

    def __init__(self):
        """Init.

        method is run as soon as an object of a class is instantiated.
        The method is useful to do any initialization you want to do
        with your object
        """
        self.client = psycopg2.connect(database="postgres", user="postgres", password="prajwal.wale", host="127.0.0.1")
        self.error = None
        self.error_code = None

    def get_bank(self, id, limit=10, offset=0, keyword=""):
        cur = self.client.cursor()
        cur.execute("SELECT * from bank WHERE ifsc='{}'".format(str(id)))
        output = cur.fetchone()
        return to_json(output)

    def get_branch(self, bank_name, city_name, limit=10, offset=0, keyword=""):
        cur = self.client.cursor()
        cur.execute("SELECT * from bank WHERE bank_name='{}' AND city='{}'".format(bank_name,city_name))
        output = cur.fetchall()
        count=len(output)
        return to_list_json(data=output,list_count=count)