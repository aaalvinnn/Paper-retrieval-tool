from flask import Flask, redirect, render_template,request, jsonify
from database import Database
app = Flask(__name__)
#定义路由地址
@app.route("/data")
#用jinjia2引擎渲染页面，并返回data.html页面
def data():
    return render_template("data.hyml")

#app的路由地址"/show"即为ajax中定义的url地址,采用POST、GET方法均可提交
@app.route("/show",methods=["GET", "POST"])
def show():
    #获取前端传入的title数据
    if request.method == "POST":
        title_name = request.form.get("title_name")
    if request.method == "GET":
        title_name = request.form.get("title_name")
    #创建Database类的对象
    sql = Database("papers")
    try:
        #执行sql语句
        result = sql.execute(f"SELECT * FROM safe1 WHERE title LIKE '%{title_name}%'")
        if(len(result)!=0):
            return {'status':'success','message':result}
        else:
            return {'status':'success','message':"无相关记录"}
    except Exception as e:
        return {'status':"error", 'message': "code error"}
    # else:
    #     if not len(result) == 0:
    #         return {'status':'success','message':result[0][0]}
    #     else:
    #         return "rbq"
@app.route("/show1",methods=["GET", "POST"])
def show1():
    #获取前端传入的No数据
    if request.method == "POST":
        No = request.form.get("No")
    if request.method == "GET":
        No = request.form.get("No")
    #创建Database类的对象
    sql = Database("papers")
    try:
        #执行sql语句
        result1 = sql.execute(f'SELECT * FROM safe1 WHERE No = {No}')
        if(len(result1)!=0):
            return {'status':'success','message':result1}
        else:
            return {'status':'success','message':"无相关记录"}
    except Exception as e:
        return {'status':"error", 'message': "code error"}
@app.route("/show_arxiv",methods=["GET", "POST"])
def show_arxiv():
    #获取前端传入的No数据
    if request.method == "POST":
        arxiv = request.form.get("arxiv")
    if request.method == "GET":
        arxiv = request.form.get("arxiv")
    #创建Database类的对象
    sql = Database("papers")
    try:
        #执行sql语句
        result_arxiv = sql.execute(f'SELECT * FROM safe1 WHERE arXiv = {arxiv}')
        if(len(result_arxiv)!=0):
            return {'status':'success','message':result_arxiv}
        else:
            return {'status':'success','message':"无相关记录"}
    except Exception as e:
        return {'status':"error", 'message': "code error"}
@app.route('/')
def root():
    return render_template('data.html')

app.run(port=8080)
