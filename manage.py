# -*- coding: utf-8 -*-
from flask_script import Manager

from ToDoList import app, db

manager = Manager(app)


@manager.command  # 只允许命令行执行该函数
def init_database():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
