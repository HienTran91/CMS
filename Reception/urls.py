from django.conf.urls import url 
 
from . import views 


urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^laboratory/', views.laboratory, name='laboratory'),
	url(r'^management/', views.management, name='management'),
	url(r'^schedule/', views.schedule, name='schedule'),
]
