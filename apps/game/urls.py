from django.urls import path,include
from .views import *

app_name='game'

urlpatterns = [
    path('',main,name='main'),
    # path('attack_main/', main, name='attack_main'),
    path('attack', attack, name ='attack'),
    path('attack_choice', attack_choice, name ='attack_choice'),
    path('attacking/<int:pk>', attacking, name ='attacking'),
    path('list/', game_list , name='list'),
#     path('detail/<int:pk>/', detail, name='detail'),
    # path('detail/<int:pk>/', detail, name='detail'),
    path('detail/', detail, name='detail'),
#     path('defend/<int:pk>/', defend, name="defend"),
    path('defend/', defend, name="defend"),
]

