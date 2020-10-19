
class FirebirdRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def run_query(self, query):
        try:
            self.cursor.execute(query)
        except Exception as ex:
            raise ex

    def fetch_results(self):
        return self.cursor.fetchall()

