from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'users/users_login.html')

def ranking(request):
    return render(request,'users/users_ranking.html')

def signup(request):
    return render(request, 'users/users_signup.html')