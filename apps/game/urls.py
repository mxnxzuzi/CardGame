from django.urls import path,include
from .views import *

app_name='game'

urlpatterns = [
    path('',main,name='main'),
    path('attack/',attack,name='attack'),
    path('list/', game_list , name='list'),
    # path('detail/<int:pk>/', detail, name='detail'),
    path('detail/', detail, name='detail'),
#     path('defend/<int:pk>/', defend, name="defend"),
    path('defend/', defend, name="defend"),
]