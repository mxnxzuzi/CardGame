from django.urls import path,include
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('attack/', attack, name ='attack'),
    path('list/', attack, name ='list'),
]

