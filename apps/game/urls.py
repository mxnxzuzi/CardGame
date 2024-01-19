from django.urls import path,include
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('attack/', attack, name ='attack'),
    path('list/', game_list, name ='list'),
    path('detail/', game_detail, name='detail'),
    path('delete/', game_delete, name='delete')
]

