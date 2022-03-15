import pymysql
class Database:
    #设置数据库连接参数
    host = 'localhost'
    user = 'root'
    password = 'Zsw,20021216'
    #构造函数
    def __init__(self,db):
        connect = pymysql.connect(host=self.host,user=self.user,password=self.password,database=db)
        self.cursor = connect.cursor()
    #类的方法(command为sql语句)
    def execute(self, command):
        try:
            self.cursor.execute(command)
        except Exception as e:
            return e
        else:
            return self.cursor.fetchall()