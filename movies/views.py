from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm, LoginUserForm
from .api_requests import *
import random


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}')

            return redirect('login')

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, user)
            return redirect('home')

    return render(request, 'login.html', {'form':form})

def home(request):
     # TRENDING MOVIES
    movie = get_trending()
    random_movie = random.randrange(0,18)
    banner = movie['results'][random_movie]
    trending = movie['results']

    # TOP RATED MOVIES
    top_rated = get_top_rated()

    # ACTION MOVIES - getting by genre_id which is 28
    action = get_genre(28)

    # COMEDY MOVIES - getting by genre_id which is 35
    comedy = get_genre(35)

    # CRIME MOVIES - getting by genre_id which is 80
    crime = get_genre(80)

    # FANTASY MOVIES - getting by genre_id which is 14
    fantasy = get_genre(14)

    # ACTION MOVIES - getting by genre_id which is 99
    documentary = get_genre(99)

    context = {
        'banner': banner,
        'trending': trending,
        'top_rated': top_rated['results'],
        'action': action['items'],
        'comedy': comedy['items'],
        'fantasy':fantasy['items'],
        'documentary': documentary['items'],

    }
    return render(request, 'index.html', context)

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return redirect('register')