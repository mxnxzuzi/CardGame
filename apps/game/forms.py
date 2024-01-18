from django import forms
from apps.users.models import User
from .models import Game

class GameForm(forms.ModelForm):
    class Meta():
        model = Game
        fields = ['attack_num', 'defend_user']
