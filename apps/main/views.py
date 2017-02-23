# - - - - - IMPORTS - - - - -

from django.shortcuts import render, redirect
from .models import User, Message, Comment

# - - - - - FUNCTIONS - - - - -

# Function to copy keys/value pairs from one dict into another
def copy(source, keys=False):
	this = {}
	if not keys:
		keys = source.keys()
	for key in keys:
		this[key] = source[key]
	return this

# Function for initializing session variables.
def seshinit(request, sesh, val=''):
	if sesh not in request.session:
		request.session[sesh] = val

# - - - - - DEVELOPER - - - - -

def dbgui(request):
	context = {
		'User'   : User.objects.all(),
		'Message': Message.objects.all(),
		'Comment': Comment.objects.all(),
	}
	return render(request, "main/dbgui.html", context)

def query(request):
	x = User.objects.filter(id=0)
	print "*"*135
	if x:
		print True
	else:
		print False
	print "*"*135
	return redirect ('/logout')

def users_delete(request, id):
	me = User.objects.filter(id=id)[0]
	me.delete()
	return redirect ('/dbgui')

def nuke(request):
	User.objects.all().delete()
	Message.objects.all().delete()
	Comment.objects.all().delete()
	return redirect ('/dbgui')

# - - - - - USERS - - - - -

def index(request): # GET
	seshinit(request, 'user_id', 0)
	if User.objects.filter(id=request.session['user_id']):
		return access(request)
	else:
		return entrance(request)

def entrance(request): # GET
	seshinit(request, 'reg_password_conf_error')
	seshinit(request, 'log_password_error')
	context = {
		'reg':{'password_conf':{'e': request.session['reg_password_conf_error']}},
		'log':{'password':{'e': request.session['log_password_error']}},
	}
	return render(request, "main/public.html", context)

def login(request): # POST
	me = User.objects.filter(email=request.POST['email'])[0]
	if request.POST['password'] == me.password:
		request.session['user_id'] = me.id
		request.session['log_password_error'] = ""
	else:
		request.session['user_id'] = 0
		request.session['log_password_error'] = "Your password is incorrect"
	return redirect ('/')

def users_create(request): # POST
	if request.POST['password'] == request.POST['password_conf']:
		me = User.objects.create(
		first_name = request.POST['first_name'],
		last_name  = request.POST['last_name'],
		email      = request.POST['email'],
		password   = request.POST['password'],
		)
	# This validation logic should really be in the model, per FMSC
		request.session['user_id'] = me.id
		request.session['reg_password_conf_error'] = ""
	else:
		request.session['user_id'] = 0
		request.session['reg_password_conf_error'] = "Passwords do not match"
	return redirect ('/')

def logout(request): # GET
	request.session.clear()
	return redirect ('/')

def access(request):
	me = User.objects.filter(id=request.session['user_id'])[0]
	context = {
		'me':me,
	}
	return render(request, "main/index.html", context)

# - - - - - MESSAGES - - - - -

def messages_create(request):
	me = User.objects.filter(id=request.session['user_id'])[0]
	Message.objects.create(
		message=request.POST['content'],
		author_id=me,
	)
	return redirect ('/')









