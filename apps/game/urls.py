from django.urls import path,include
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('attack/<int:pk>/', attack, name ='attack'),
]
