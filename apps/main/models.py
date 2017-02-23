from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class UserManager(models.Manager):
# 	def __init__(self, **kwargs):
# 		pass

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name  = models.CharField(max_length=255)
	email      = models.CharField(max_length=255)
	password   = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# manager    = UserManager()

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