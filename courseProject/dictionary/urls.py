from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),

    path('authorization/', views.loginUser, name='login'),
    path('authorization/login', views.loginUser, name='login'),
    path('authorization/register', views.register, name='register'),
    path('authorization/logout', views.logoutUser, name='logout'),

    path('dictionary/word/create', views.createWord, name='word-create')
]