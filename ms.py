from sqlite3 import connect
import mysql.connector
#连接数据库
config = {
    'user' : 'root',
    'password' : 'Zsw,20021216',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'Papers'
}
con = mysql.connector.connect(**config)
#创建游标
mycursor = con.cursor(buffered = True)

#检查表存在函数
def tableExists(mycursor, name):
    stmt = "SHOW TABLES LIKE '"+name+"'"
    mycursor.execute(stmt)
    return mycursor.fetchone()

#删除表函数
def dropTable(mycursor, name):
    stmt = "DROP TABLE IF EXISTS" +name
    mycursor.execute(stmt)

#增添整条数据
def add_data(mycursor,val):
    sql = 'INSERT INTO safe1(arXiv,title,authors,date,subjects) VALUES(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,val)
    con.commit()
#更改一条中某个字段的数据
def modify_data(mycursor,field,old_data,new_data):
    sql = f"UPDATE safe1 SET {field}='{new_data}' WHERE {field}= '{old_data}'"
    mycursor.execute(sql)
    con.commit()
#删除某条数据记录函数
def delete_data(mycursor,field,val):
    sql = f"DELETE FROM safe1 WHERE {field}= '{val}'"
    mycursor.execute(sql)
    con.commit()
#显示当前数据库信息
def search_all_data(mycursor):
    print('arXiv title authors date subjects')
    sql = 'SELECT * FROM safe1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
#查找某条记录（草稿，可以传参）
def search_data(mycursor):
    sql = 'SELECT * FROM safe1 WHERE No < 30'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#模糊查找(field：字段；val：部分字符)(LIKE函数不区分大小写)
def fuzzy_check(mycursor,field,val):
    sql = f"SELECT * FROM safe1 WHERE {field} LIKE '%{val}%'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if(len(myresult)!=0):
        for x in myresult:
            print(x)
    else:
        print('无相关结果')
    
fuzzy_check(mycursor,'title','computer')
#断开数据库，释放资源
con.close()


