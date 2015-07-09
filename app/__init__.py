#-*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import load_config
from flask import current_app

app = Flask(__name__,instance_path='F:/flask study/restful_demo1/instance')

config = load_config()
app.config.from_object(config)
#如何使用配置文件中的常量
#print app.config.get('CSRF_ENABLED')
db = SQLAlchemy(app)


from app import views,models