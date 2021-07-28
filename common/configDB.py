import pymysql
import readConfig as readConfig


localReadConfig = readConfig.ReadConfig()

host = localReadConfig.get_mysql("host")
username = localReadConfig.get_mysql("username")
password = localReadConfig.get_mysql("password")
port = localReadConfig.get_mysql("port")
database = localReadConfig.get_mysql("database")


class MyDB(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect_db(self):
        try:
            # connect to DB
            self.db = pymysql.connect(host=host, user=username, password=password, database=database, port=int(port),
                                      charset='utf8')
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            print(ex)

    def execute_sql(self, sql2, params2):
        # executing sql
        self.cursor.execute(sql2, params2)
        # executing by committing to DB
        self.cursor.close()

    def run(self, sql1, params1):
        self.connect_db()
        self.execute_sql(sql1, params1)
        value = self.cursor.fetchall()
        for i in value:
            print(i)
        self.close_db()
        return value

    def close_db(self):
        self.db.commit()
        self.db.close()
        print("Database closed!")


if __name__ == '__main__':
    my_db = MyDB()
    sql = """
        SELECT * FROM `tt_vehicle_price_limit` t WHERE t.`product_code` = %s AND t.`entity_code` = %s
    """
    params = ('FPZ-000006 FWS-000003 FNS-000003', 'HD340400')
    my_db.run(sql, params)




