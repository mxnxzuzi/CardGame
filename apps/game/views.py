from django.shortcuts import render,redirect

def main(request):
    return render(request,'game/game_main.html')

def attack(request):
    return render(request,'game/game_attack.html')

def game_list(request):
    return render(request, 'game/game_list.html')

def login(request):
    return render(request, 'game/game_login.html')

# Create your views here.
