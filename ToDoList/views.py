# -*-encoding=utf8-*-
import json
import os
import sys
from datetime import datetime

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


@app.route('/addlist/', methods={'post'})
def add_list():
    content = request.values['content']
    print content
    li = List(content)
    db.session.add(li)
    db.session.commit()
    return ""
