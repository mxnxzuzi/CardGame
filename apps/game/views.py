from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.users.models import User
from .models import *
import random
from .forms import GameForm

def main(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.attack_user = request.user 
            game.save()
            return redirect('game:attack', pk=game.id)
    else:
        form = GameForm()

    ctx = {'form': form}
    return render(request, 'game/game_main.html', ctx)



def attack(request, pk):
    game = Game.objects.get(id=pk)
    ctx = {'game': game}
    
    if game.attack_num == 0 or game.defend_num == 0:
        game.game_now = False
    else :
        if game.game_num == 1:
            # 게임 1: 수가 클 때 이기는 게임
            if game.attack_num > game.defend_num:
                ctx['game_result'] = "수가 클 때 이깁니다! {}승!".format(game.attack_user)
            else:
                ctx['game_result'] = "수가 클 때 이깁니다! {}승!".format(game.defend_user)
        else:
            # 게임 2: 수가 작을 때 이기는 게임
            if game.attack_num < game.defend_num:
                ctx['game_result'] = "수가 작을 때 이깁니다! {}승!".format(game.attack_user)
            else:
                ctx['game_result'] = "수가 작을 때 이깁니다! {}승!".format(game.defend_user)
        
        game.game_now = True
    game.save()
    return render(request, 'game/game_attack.html', ctx)
