from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Game(models.Model):
    now = models.BooleanField('경기상태', default=False)
    attack_num = models.IntegerField('공격숫자', default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    defend_num = models.IntegerField('수비숫자', default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    attack_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attack_games', verbose_name='공격자')
    defend_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='defend_games', verbose_name='수비자')
