from django.conf.urls import url
from . import views

urlpatterns = [
	# Dev
	url(r'^dbgui$', views.dbgui),
	url(r'^query$', views.query),
	url(r'^nuke$', views.nuke),

	# App
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^logout$', views.logout),

	url(r'^.*$', views.index),
]
