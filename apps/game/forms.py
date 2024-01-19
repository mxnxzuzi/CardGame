from django import forms
from apps.users.models import User
from .models import Game
import random

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['attack_num', 'defend_user']

    # def __init__(self, *args, **kwargs):
    #     super(GameForm, self).__init__(*args, **kwargs)
    #     current_user = self.initial.get('current_user', None)
    #     if current_user:
    #         self.fields['defend_user'].queryset = User.objects.exclude(id=current_user.id)
    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        random_choices = random.sample(range(1, 11), 5)  # 1~10 중 무작위로 5개 선택
        self.fields['attack_num'].widget = forms.Select(choices=[(i, str(i)) for i in random_choices])
