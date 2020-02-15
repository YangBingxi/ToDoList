# -*-encoding=utf8-*-
import sys

from flask import render_template, request

from ToDoList import app, db
from ToDoList.models import List

# 解决用户名中文输入的问题
reload(sys)
sys.setdefaultencoding('utf-8')


@app.route("/")
def index():
    lists = List.query.order_by(db.desc(List.id)).all()
    return render_template('index.html', lists=lists)


@app.route('/addlist/', methods={'post', 'get'})
def add_list():
    content = request.values['content']
    print content
    li = List(content)
    db.session.add(li)
    db.session.commit()
    return ""


@app.route('/changestatus/', methods={'post', 'get'})
def change_status():
    status = request.values['status']
    list_id = request.values['list_id']
    print status, list_id
    db.session.query(List).filter(List.id == list_id).update({"status": status})
    db.session.commit()
    return ""
