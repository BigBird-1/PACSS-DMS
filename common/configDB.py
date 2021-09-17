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

    def create_table(self, create_sql):
        self.connect_db()
        self.cursor.execute(create_sql)
        self.cursor.close()
        self.close_db()

    def run(self, sql1, params1):
        self.connect_db()
        self.execute_sql(sql1, params1)
        # value = self.cursor.fetchall()
        # print(value)
        self.close_db()
        # return value

    def close_db(self):
        self.db.commit()
        self.db.close()
        print("Database closed!")


my_db = MyDB()


if __name__ == '__main__':
    # sql_createTb = """CREATE TABLE test_340400 (
    #                  id INT NOT NULL AUTO_INCREMENT,
    #                  token  CHAR(50),
    #                  user_name CHAR(25),
    #                  user_id INT,
    #                  PRIMARY KEY(id))
    #                  """

    sql = """alter table test_340400 ADD COLUMN position_code CHAR(20)"""
    my_db.create_table(sql)

    # sql = """
    #         INSERT INTO test_340400 VALUES(%s,%s,%s,%s);
    #     """
    # params = (3, 'Bearer 67e2b19f-5465-4953-bc29-c91b0e754970', '销售一', '88880000002689')
    # my_db.run(sql, params)





