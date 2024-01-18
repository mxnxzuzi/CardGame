# Generated by Django 5.0.1 on 2024-01-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now', models.BooleanField(verbose_name='경기상태')),
                ('attack_num', models.IntegerField(default=0, verbose_name='공격숫자')),
                ('defend_num', models.IntegerField(default=0, verbose_name='수비숫자')),
            ],
        ),
    ]
