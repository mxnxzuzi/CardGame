from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Game(models.Model):
    now = models.BooleanField('경기상태')
    attack_num = models.IntegerField('공격숫자', default = 0,  validators=[MinValueValidator(1), MaxValueValidator(10)])
    defend_num = models.IntegerField('수비숫자', default = 0,  validators=[MinValueValidator(1), MaxValueValidator(10)])
    #공격자 나중에 users에서 foreign
    #수비자 나중에 users에서 foreign
    attack_user = models.CharField('공격자', max_length = 20)
    defend_user = models.CharField('수비자', max_length = 20)