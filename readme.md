# my todo-list

- [En](#based on python,flask and mysql)
- [中文]

---

## Create your TODO-List

## based on python,flask and mysql

- python2.7
- flask1.1.1
- SQLAlchemy3.0
- **mysql5.7**

---

## Demo:

![play](ToDoList/img/todolist.gif)
---



---

## Guide

### Add a list:

insert the content in ```Title```,then click the button ```Add```.

### Mark done

click the list which you had done.

### Make TOP

click the button ```置顶```, you can make it TOP.

### Make UN-TOP

click the button ```取消置顶```, you can make it UN-TOP.

### Delete

if you use pc browse website, you can click on right,then click ```ok``` make sure.

if you use mobile browse website, you can press long time to delete it.

### The TIMELINE

use different color to mark each list

- blue: TOP
- green: Done
- yellow: Need to do
- red: Delete

---

## Make it on your computer

### you can use it on your computer

- git clone to local:
```git clone https://github.com/youngsw/ToDoList.git```
- use pycharn to open it.
- chang database to yourself
  - the config about database is ```/ToDoList/app.conf```
- when you create database of todolist, you need to init it.
  - ```python2 manage.py init_database```
---

### It also recommended run on a server

- git clone to your server:
```git clone https://github.com/youngsw/ToDoList.git```
- cd to project file
```cd ToDoList/```

- chang database to yourself
  
  - the config about database is ```/ToDoList/app.conf```
- when you create database of todolist, you need to init it.
  
- ```python2 manage.py init_database```
  
- use gunicorn to run the project (attention : on server)
  ```gunicorn -w 1 -b 127.0.0.1:8002 ToDoList:app #set port 8002```

- set nginx 
  - Reverse request to local port 127.0.0.1:8002
  - ```bash
    # /etc/nginx/site-available/default
    server {
        listen 80;
        server_name yourdomainname; # attention:change to your domain name
        location / {
            proxy_pass http://127.0.0.1:8002;
        }
    }
    ```



---

## 搭建自己的 TODO-List

### 环境：

- **Python2.7**
- **Flask1.1.1**
- **SQLAlchemy3.0**
- **mysql5.7**

### 演示

![Demo](ToDoList/img/todolist.gif)

### 使用指南

#### 添加List事项

在```Title```文本输入框内事项，点击```add```添加按钮即可。

#### 将事项标记为已完成

在该事项上单击即可

#### 将事项设置为置顶

点击该事项后的```置顶```按钮即可

#### 将已置顶的事项取消置顶

点击该事项后的```取消置顶```即可

#### 删除该事项

如果使用pc端访问的话，先右击，在弹框进行确认就可以删除

如果使用的时移动端，试着长按

### Timeline-时间线

使用不同的颜色代表不同状态的事项

- 蓝色：置顶
- 黄色：已完成
- 黄色：等待完成
- 红色：已删除

