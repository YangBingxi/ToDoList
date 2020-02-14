# -*-encoding=utf8-*-
from datetime import datetime

from ToDoList import db


class User(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}  # 设置表的编码格式为utf8
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 用户id：整形、主键、自增
    username = db.Column(db.String(80), unique=True)  # 用户名：字符串类型、唯一
    password = db.Column(db.String(32))  # 用户密码

    def __init__(self, username, password):
        self.username = username
        self.password = password


class List(db.Model):
    # __table_args__ = {'mysql_collate': 'utf8_general_ci'}  # 设置表的编码格式为utf8
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id：整形、主键、自增
    content = db.Column(db.String(1024))
    create_date = db.Column(db.DateTime)  # 图片创建时间
    status = db.Column(db.Integer, default=1)

    '''
    类的构造函数
    '''

    def __init__(self, content, status, create_date):
        self.content = content
        self.status = status
        self.create_date = datetime.now()
