from django import forms
from apps.users.models import User
from .models import Game
import random

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['attack_num','defend_user']

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None) 
        super(GameForm, self).__init__(*args, **kwargs)
    
        if current_user:
            self.fields['defend_user'].queryset = User.objects.exclude(id=current_user.id)
    
        random_choices = random.sample(range(1, 11), 5)
        self.fields['attack_num'].widget = forms.Select(choices=[(i, str(i)) for i in random_choices])

class DefendForm(forms.ModelForm):
    class Meta:
        model=Game
        fields = ['defend_num']

    def __init__(self, *args, **kwargs):
        super(DefendForm, self).__init__(*args, **kwargs)
        random_choices = random.sample(range(1, 11), 5)
        self.fields['defend_num'].widget = forms.Select(choices=[(i, str(i)) for i in random_choices])