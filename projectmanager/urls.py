from unicodedata import name
from . import views
from django.urls import path, include


urlpatterns = [

path('', views.home, name='home'),
path('add_project', views.add_project, name='add_project'),
path('registerUser', views.registerUser, name='registerUser'),
path('loginUser', views.loginUser, name='loginUser'),
path('logoutUser', views.logoutUser, name='logoutUser'),
path('delete_project/<str:pk>', views.deleteProject, name='delete_project'),
path('complete_project/<str:pk>', views.completeProject, name="complete_project" ),
path('add_task', views.add_task, name='add_task'),
path('completeTask/<str:pk>', views.completeTask, name="completeTask"),
path('delete_task/<str:pk>', views.deleteTask, name='deleteTask'),



]