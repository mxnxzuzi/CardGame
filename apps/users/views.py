from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import *

# Create your views here.
def main(request):
    return redirect('game:main')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('game:main')
        else:
            # 유효하지 않은 데이터 처리
            ctx={
                'form':form,
            }           
            return render(request,'users/users_signup.html', ctx)
    else:
        form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, 'users/users_signup.html',context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            if request.user.nickname==None or request.user.nickname=="":
                return render(request, "users/users_setname.html")
            else:
                return redirect('users:main')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name='users/users_login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='users/users_login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('game:main')

def ranking(request):
    rankers=User.objects.order_by("-points")[:5]
    return render(request, "users/users_ranking.html", {'rankers':rankers})

def set_name(request):
    if request.method=="POST":
        user=request.user
        new_name=request.POST["name"]
        if User.objects.filter(nickname=new_name):
            return render(request, "users/users_setname.html", {'error':"이미 존재하는 닉네임 입니다!"})
        else:
            user.nickname=new_name
            user.save()
            return redirect("users:main")
    if request.user.nickname==None or request.user.nickname=="":
        return render(request, "users/users_setname.html")
    else:
        return redirect('game:main')
    
