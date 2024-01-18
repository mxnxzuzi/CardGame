from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Game
import random

def main(request):
    games = Game.objects.all()
    options = random.sample(range(1, 11), 5)
    ctx = {'games': games, 'options': options}
    return render(request, 'game/game_main.html', ctx)

def attack(request, pk):
    game = Game.objects.get(id=pk)
    ctx = {'game': game}
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option', None)
        
        if selected_option is not None:
            game.attack_num = int(selected_option) # 만약 selected_option이 정수라면
            game.save() # game 객체 업데이트
    return render(request, 'game/game_attack.html', ctx)
