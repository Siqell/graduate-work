from django.urls import path
from . import views


app_name = 'mainpage'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('about/', views.about, name = 'about'),
	path('profile/', views.profile, name = 'profile'),
	path('account/registration/', views.regpage, name = 'regpage'),
	path('signup/', views.signup, name = 'signup'),
]