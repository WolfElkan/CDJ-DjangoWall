from django.conf.urls import url
from . import views

urlpatterns = [
	# Dev
	url(r'^dbgui$', views.dbgui),
	url(r'^query$', views.query),
	url(r'^nuke$', views.nuke),

	# Users
	url(r'^login$', views.login),
	url(r'^register$', views.users_create),
	url(r'^logout$', views.logout),
	url(r'^users/delete/(?P<id>\d+)$', views.users_delete),

	# Messages
	url(r'^messages/create$', views.messages_create),

	# Comments
	url(r'^comments/create$', views.comments_create),

	url(r'^.*$', views.index),
]
