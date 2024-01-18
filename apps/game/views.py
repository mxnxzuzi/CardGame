from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.users.models import User
from .models import *
import random

def main(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        selected_user_id = request.POST.get('selected_user')
        
        if selected_option and selected_user_id:
            # 선택한 사용자와 옵션을 사용하여 Game 객체 생성
            selected_user = User.objects.get(id=selected_user_id)
            game = Game.objects.create(defend_user=selected_user, attack_num=selected_option,  attack_user=request.user)
            
            return redirect('game:attack', pk=game.id)
    
    # GET 요청이거나 선택된 값이 없는 경우
    user = request.user
    other_users = User.objects.exclude(id=user.id)
    games = Game.objects.all()
    options = random.sample(range(1, 11), 5)
    ctx = {'users': other_users, 'options': options, 'games': games}
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
