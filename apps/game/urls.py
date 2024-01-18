from django.urls import path,include
from .views import *

app_name='game'

urlpatterns = [
    path('',main,name='main'),
    path('login/', login, name='login'),
    path('attack/',attack,name='attack'),
    path('list/', game_list , name='list'),
#     path('detail/<int:pk>/', detail, name='detail'),
#     path('defend/<int:pk>/', defend, name="defend"),
#     path('delete/<int:pk>/', delete, name="delete"),
#     path('ranking/', ranking, name='ranking'),
]