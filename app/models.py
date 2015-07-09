#-*-coding:utf-8-*-
from app import db,app
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
class Tasks(db.Model):
	__tablename__='tasks'
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(60))
	done = db.Column(db.Boolean,default=False)
	description = db.Column(db.String(120))
	uri = db.Column(db.String(60))

	def __unicode__(self):
		return '<tasks %r>' % (self.title)

	def __repr__(self):
		return '<tasks %r>' % (self.title)	
		
	def todict(self):
		return {'id':self.id,'title':self.title}	

class User(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(32),index=True)
	password_hash = db.Column(db.String(128))

	def hash_password(self,password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self,password):
		return pwd_context.verify(password,self.password_hash)

	def generate_auth_token(self):
		
		s = Serializer(app.config['SECRET_KEY'])
		return s.dumps({'id':self.id})

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			print type(token)
			data = s.loads(token)

		except:
			#print 'aaa'
			return None
		
		user = User.query.get(data['id'])
		
		return user
