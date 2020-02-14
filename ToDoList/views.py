# -*-encoding=utf8-*-
import json
import os
import sys
from datetime import datetime

from flask import render_template, request

from ToDoList import app, db
from ToDoList.models import List



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
