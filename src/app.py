from flask import Flask, render_template,request, redirect, url_for
from .database import Database
from .models import Post

# 创建 Flask 应用实例
app = Flask(__name__)
# 创建数据库对象，指定数据库文件路径
db = Database("blog.db")

# 初始化数据库
db.create_table()