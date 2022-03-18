from sqlite3 import connect
import mysql.connector
#连接数据库
class Database(object):
    #构造函数
    def __init__(self):
        #设置数据库参数
        config = {
        'user' : 'root',
        'password' : 'Zsw,20021216',
        'host' : 'localhost',
        'port' : '3306',
        'database' : 'papers'
    }
        self.con = mysql.connector.connect(**config)
        #创建游标
        self.mycursor = self.con.cursor(buffered = True)
    #检查表存在函数
    def tableExists(self, name):
        stmt = "SHOW TABLES LIKE '"+name+"'"
        self.mycursor.execute(stmt)
        return self.mycursor.fetchone()

    #删除表函数
    def dropTable(self, name):
        stmt = "DROP TABLE IF EXISTS" +name
        self.mycursor.execute(stmt)
        self.con.commit()

    #增添整条数据
    def add_data(self,val):
        sql = 'INSERT INTO safe1(arXiv,title,authors,date,subjects,address) VALUES(%s,%s,%s,%s,%s,%s)'
        self.mycursor.execute(sql,val)
        self.con.commit()
    #更改一条中某个字段的数据
    def modify_data(self,field,old_data,new_data):
        sql = f"UPDATE safe1 SET {field}='{new_data}' WHERE {field}= '{old_data}'"
        self.mycursor.execute(sql)
        self.con.commit()
    #删除某条数据记录函数
    def delete_data(self,field,val):
        sql = f"DELETE FROM safe1 WHERE {field}= '{val}'"
        self.mycursor.execute(sql)
        self.con.commit()
    #显示当前数据库信息
    def search_all_data(self):
        print('arXiv title authors date subjects')
        sql = 'SELECT * FROM safe1'
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
    #查找某条记录（草稿，可以传参）
    def search_data(self,field,val):
        sql = f'SELECT * FROM safe1 WHERE {field} = {val}'
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            return(x)

    #模糊查找(field：字段；val：部分字符)(LIKE函数不区分大小写)
    def fuzzy_check(self,field,val):
        sql = f"SELECT * FROM safe1 WHERE {field} LIKE '%{val}%'"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        if(len(myresult)!=0):
            for x in myresult:
                print(x)
        else:
            print('无相关结果')

abc = Database()
for i in range(15327,53223):
    abc.delete_data('No',i)


