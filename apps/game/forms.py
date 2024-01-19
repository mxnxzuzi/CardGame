from django import forms
from apps.users.models import User
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['attack_num', 'defend_user']

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None) 
        super(GameForm, self).__init__(*args, **kwargs)
        if current_user:
            self.fields['defend_user'].queryset = User.objects.exclude(id=current_user.id) 
