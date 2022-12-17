from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),

    path('authorization/', views.loginUser, name='login'),
    path('authorization/login', views.loginUser, name='login'),
    path('authorization/register', views.register, name='register'),
    path('authorization/logout', views.logoutUser, name='logout'),

    path('dictionary/', views.dictionaryGet, name='dictionary'),
    path('dictionary/word/create', views.createWord, name='word-create'),
    path('dictionary/word/create/<int:fields>', views.createWord, name='word-create'),
    path('dictionary/word/delete/<int:word_id>', views.deleteWord, name='word-delete'),
    path('dictionary/word/details/<int:word_id>', views.detailsWord, name='word-details'),
]