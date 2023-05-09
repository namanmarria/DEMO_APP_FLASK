import mysql.connector as ck
class orders:

    def __init__(self):
        self.connection = ck.connect(user='root', password='admin123', host='127.0.0.1', database='demo')
        print("CK CONNECTED : ")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED ")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED : ")

    def read(self, sql):
        self.cursor.execute(sql)
        print("SQL QUERY EXECUTED : ")
        rows = self.cursor.fetchall()
        return rows