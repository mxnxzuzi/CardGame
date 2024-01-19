from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.users.models import User
from .models import *
import random
from .forms import GameForm


def main(request):
    return render(request, 'game/game_main.html')
def game_list(request):
    return render(request, 'game/game_list.html')

def detail(request):
    return render(request, 'game/game_detail.html')

def defend(request):
    return render(request, 'game/game_defend.html')

def attack(request):
    return render(request, 'game/game_attacking.html')

def attack_choice(request):
    if request.method == 'POST':
        form = GameForm(request.POST, current_user=request.user)
        if form.is_valid():
            game = form.save(commit=False)
            game.attack_user = request.user 
            game.save()
            return redirect('game:attacking', pk=game.id)
    else:
        form = GameForm(current_user=request.user)

    games = Game.objects.all()
    game = games.last()  # 가장 최근에 생성된 게임 객체를 가져옵니다.
    ctx = {'games': games, 'form': form, 'game': game}
    return render(request, 'game/game_attack.html', ctx)



def attacking(request, pk):
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
    return render(request, 'game/game_attacking.html', ctx)

