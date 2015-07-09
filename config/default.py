#-*-coding:utf-8-*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

"""
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@10.66.18.80:3306/rest_demo1'
"""
class Config(object):
	DEBUG = True
	CSRF_ENABLED = True
	SECRET_KEY = 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = 'mysql://user:pwd@00.00.00.00:0000/rest_demo1'
