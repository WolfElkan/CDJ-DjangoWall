from __future__ import unicode_literals
from django.db import models
from . import supermodel

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name  = models.CharField(max_length=255)
	email      = models.CharField(max_length=255)
	pw_hash    = models.CharField(max_length=60)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	fields = ['first_name','last_name','email','pw_hash']
	validations = [
		
	]
	objects = supermodel.Manager('main','User', fields, validations)

class Message(models.Model):
	author_id  = models.ForeignKey(User)
	message    = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	author_id  = models.ForeignKey(User)
	message_id = models.ForeignKey(Message)
	comment    = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)