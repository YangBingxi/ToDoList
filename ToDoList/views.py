# -*-encoding=utf8-*-
import sys

from flask import render_template, request

from ToDoList import app, db
from ToDoList.models import List

# reload(sys)
# sys.setdefaultencoding('utf-8')


@app.route("/")
def index():
    #lists = List.query.order_by(db.desc(List.id)).all()
    return render_template('index.html')


@app.route("/pc")
def index_pc():
    lists = List.query.order_by(db.desc(List.id)).all()
    return render_template('index_pc.html', lists=lists)


@app.route("/mobile")
def index_mobile():
    lists = List.query.order_by(db.desc(List.id)).all()
    return render_template('index_mobile.html', lists=lists)


@app.route("/timeline")
def timeline():
    lists = List.query.order_by(db.desc(List.id)).all()
    return render_template('timeline.html', lists=lists)


@app.route('/addlist/', methods={'post', 'get'})
def add_list():
    content = request.values['content']
    li = List(content)
    db.session.add(li)
    db.session.commit()
    return ""


@app.route('/changestatus/', methods={'post', 'get'})
def change_status():
    status = int(request.values['status'])
    list_id = int(request.values['list_id'])
    # print status, list_id
    li = List.query.filter_by(id=list_id)
    if status == 6:
        li.update({"status": 6})
    elif status == 7:
        li.update({"status": 2})
    elif status == 5 and li[0].status == 1:
        li.update({"status": 2})
    elif status == 5 and li[0].status == 2:
        li.update({"status": 1})
    elif status == 0:
        li.update({"status": 0})
    db.session.commit()
    return ""
