#-*-coding:utf-8-*-
from flask import Flask,render_template,jsonify,request,abort,g
from flask_sqlalchemy import Pagination
from app import app,db
from .models import Tasks,User
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
@auth.verify_password
def verify_password(username_or_token,password):
	user = User.verify_auth_token(username_or_token)
	
	if not user:
		user = User.query.filter_by(username=username_or_token).first()
		if not user or not user.verify_password(password):
			return False
	g.user = user
	return True

@app.route('/todo/api/tasks/page=<int:page>&size=<int:size>',methods=['GET'])
def get_tasks(page,size):
	result = Tasks.query.filter_by(done=1).paginate(page,size,False)
	tasks = result.items
	l = []
	for i in tasks:

		j=i.todict()
		l.append(j)

	return jsonify({'tasks':l,'total':result.pages,'prev':result.prev_num,'next':result.next_num})

@app.route('/todo/api/account/register',methods=['POST'])
def new_user():
	username = request.form.get('username',None)
	password = request.form.get('password',None)
	print request.json
	print password
	if username is None or password is None:
		abort(400)
	if User.query.filter_by(username=username).first() is not None:
		abort(400)
	user = User(username=username)
	user.hash_password(password)
	db.session.add(user)
	db.session.commit()
	return jsonify({'id':user.id})

@app.route('/todo/resource')
@auth.login_required
def get_resource():

	return jsonify({'data':'hello'})

@app.route('/api/token')
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token()
	
	return jsonify({'token':token.decode('ascii')})