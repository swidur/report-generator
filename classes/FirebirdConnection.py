from fdb import connect


class FirebirdConnection:
    def __init__(self, path, host='127.0.0.1', user='sysdba', pw='masterkey'):
        self.connection = None
        self.user = user
        self.pw = pw
        self.host = host
        self.path = path

    def connect(self):
        try:
            self.connection = connect(host=self.host, database=self.path, user=self.user, password=self.pw, charset="UTF-8")
        except Exception as ex:
            raise ex

        return self.connection

