from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.users.models import User
from .models import *
import random
from .forms import *
from django.contrib import auth

def main(request):
    return render(request, 'game/game_main.html')

def defend(request, pk):
    game = Game.objects.get(id=pk)
    if request.method == 'GET':
        counter = request.GET.get('counter', None)
        form = DefendForm(instance=game)
        ctx = {
            'form': form,
            'pk': pk,
            'counter': counter
        }
        return render(request, 'game/game_defend.html', ctx)
    form = DefendForm(request.POST, instance=game)
    if form.is_valid():
        form.save()
    game.now = True
    game.save()

    counter = request.POST['counter']
    users = User.objects.all()
    user_game = Game.objects.get(id=pk)
    user_nickname = auth.get_user(request).nickname
    user_num = 0
    enemy = ''
    enemy_num = 0
    winner=''

    if user_game.attack_user.nickname == user_nickname:
        user_num = user_game.attack_num
        enemy = user_game.defend_user.nickname
        enemy_num = user_game.defend_num
    else:
        user_num = user_game.defend_num
        enemy = user_game.attack_user.nickname
        enemy_num = user_game.attack_num

    if user_game.game_num == 1:
        if user_num < enemy_num:
            winner = user_nickname
        elif user_num > enemy_num:
            winner = enemy
    else:
        if user_num < enemy_num:
            winner = enemy
        elif user_num > enemy_num:
            winner = user_nickname

    me = users.get(nickname=user_nickname)
    other = users.get(nickname=enemy)
    if winner == user_nickname:
        me.points += user_num
        other.points -= enemy_num
    elif winner == enemy:
        me.points -= user_num
        other.points += enemy_num

    me.save()
    other.save()

    return redirect(f'../detail/{pk}?counter={counter}')

def attack(request):
    return render(request, 'game/game_attacking.html')

def attack_choice(request):
    if request.method == 'POST':
        form = GameForm(request.POST, current_user=request.user)
        if form.is_valid():
            game = form.save(commit=False)
            game.attack_user = request.user
            game.save()
            return redirect('game:list')
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

def game_list(request):
    games = Game.objects.all()
    user_id = auth.get_user(request).id
    user_games = games.filter(models.Q(attack_user=user_id) | models.Q(defend_user=user_id))
    user_games = user_games.order_by("-id")
    ctx = {
        'user_games': user_games
    }
    return render(request, 'game/game_list.html', ctx)

def game_detail(request, pk):
    users = User.objects.all()
    user_game = Game.objects.get(id=pk)
    user_nickname = auth.get_user(request).nickname
    counter = request.GET.get('counter', None)
    user_num = 0
    enemy = ''
    enemy_num = 0
    winner=''

    if user_game.attack_user.nickname == user_nickname:
        user_num = user_game.attack_num
        enemy = user_game.defend_user.nickname
        enemy_num = user_game.defend_num
    else:
        user_num = user_game.defend_num
        enemy = user_game.attack_user.nickname
        enemy_num = user_game.attack_num

    if user_game.game_num == 1:
        if user_num < enemy_num:
            winner = user_nickname
        elif user_num > enemy_num:
            winner = enemy
    else:
        if user_num < enemy_num:
            winner = enemy
        elif user_num > enemy_num:
            winner = user_nickname

    ctx = {
        'user_game': user_game,
        'counter': counter,
        'user_num': user_num,
        'enemy': enemy,
        'enemy_num': enemy_num,
        'winner': winner
    }
    return render(request, 'game/game_detail.html', ctx)

def game_delete(request, pk):
    if request.method == 'POST':
        user_game = Game.objects.get(id=pk)
        user_game.delete()
    return redirect("game:list")
