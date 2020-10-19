

class SqlValidator:
    def __init__(self):
        pass

    def is_sql_select(self, sql):
        """
        Checks if supplied sql is a select.
        :param sql:
        :return:
        """
        sql = sql.strip().lower()
        forbidden = ["delete from", "insert into", "update", "drop table", "drop view", "alter table", "alter", "drop",
                     "truncate", "create"]

        if not sql.startswith("select"):
            return False
        for clause in forbidden:
            if sql.startswith(clause):
                return False
        return True




