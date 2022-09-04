from django.shortcuts import render, redirect
from .models import Player, Team, Position
from .forms import PlayerForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import datetime


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist.')

    context = {'page':page}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            #user.save()
            user = User.objects.create(
                username=request.POST.get('username'),
                password=request.POST.get('password1')
            )
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error ocurred during registration.')

    context = {'page':page,'form':form}
    return render(request, 'base/login.html', context)


def home(request):
    teams = Team.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    players = Player.objects.filter(
        Q(team__name__icontains = q) | 
        Q(name__icontains = q))
    context = {'players': players, 'teams':teams, 'players_count':players.count()}
    return  render(request, 'base/home.html',context)

def player(request, pk):
    player = Player.objects.get(id=pk)
    positions = player.positions.all()
    team_players = player.team.player_set.all()
    context = {'player':player, 'team_players': team_players, 'positions':positions}
    return render(request, 'base/player.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    print(context)
    return render(request,'base/user-profile.html', context)

@login_required(login_url='/login')
def createPlayer(request):
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            #player = form.save(commit=False)
            #player.created_by = request.user
            #form.save()
            player = Player.objects.create(
                name = request.POST.get('name'),
                description = request.POST.get('description'),
                date_of_birth = datetime.datetime.strptime(request.POST.get('date_of_birth'),"%d/%m/%Y").date(),
                team = Team.objects.get(id=request.POST.get('team')),
                created_by = request.user,
            )
            positions = request.POST.getlist('positions')
            for p in positions:
                position = Position.objects.get(id=int(p))
                player.positions.add(position)
            return redirect('home')


    context = {'form':form}
    return render(request, 'base/player_form.html', context)

@login_required(login_url='/login')
def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)

    if request.user != player.created_by:
        messages.error(request, 'You can not edit the player {}.'.format(player.name))
        return redirect('home')

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/player_form.html', context)

@login_required(login_url='/login')
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    if request.user != player.created_by:
        messages.error(request, 'You can not edit the player {}.'.format(player.name))
        return redirect('home')
    if request.method == 'POST':
        player.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':player})

