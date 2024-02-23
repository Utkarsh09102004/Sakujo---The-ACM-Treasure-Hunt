from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .algos import *
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib import messages



def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins')
    else:
        form = SignUpForm()
    return render(request, 'base/signup_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.userprofile.team is None:
                    return redirect('team')
                else:
                    return redirect('team-details')
            else:
                return HttpResponse("Hatt Bhsdk")
    else:
        form = AuthenticationForm()
    return render(request, 'base/login_user.html', {'form': form})

def account_view(request):
    return render(request, 'base/account.html')

@login_required(login_url='account')
def jcteam(request):
    return render(request, 'base/team.html')

@login_required(login_url='account')
def create_team(request):
    sec_code = generate_random_string(8)
    users = request.user.userprofile
    if request.method == 'POST':
        team_name = request.POST.get('teamName')
        # storyline_name = random.choice(["story-1", "story-2"])  # Randomly select a storyline
        storyline_name="story-1"
        team = Team.objects.create(name=team_name, sec_code=sec_code)
        storyline = Storyline.objects.get(name=storyline_name)
        if storyline_name == "story-1":
            clue_id = 1
        else:
            clue_id = 8
        clue = Clue.objects.get(id=clue_id)

        team.current_clue = clue
        team.storyline = storyline
        team.save()

        users.team = team
        users.save()
        return redirect('team-details')

    context={'sec_code':sec_code}
    return render(request, 'base/create_team.html',context)

from django.contrib import messages

@login_required(login_url='account')
def join_team(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        code = request.POST.get('secCode')
        team = Team.objects.filter(sec_code=code).first()

        if team is None:
            messages.warning(request, "Incorrect code")
        elif team.userprofile_set.count() >= 3:  # Check if the team is full (more than or equal to 5 members)
            messages.warning(request, "Team is full. Cannot join.")
        else:
            user_profile.team = team
            user_profile.save()
            return redirect('team-details')

    return render(request, 'base/join_team.html')
@login_required(login_url='account')
@csrf_exempt
def clue_render(request):
    team =request.user.userprofile.team
    clues=team.current_clue
    print(clues.id)

    if (clues.id == 2 ):
        if (team.summon == 'reached'):
            return redirect('center-game')

    if (clues.id == 5):
        if (team.hangman == 'reached'):
            return redirect('hangman')

    if (clues.id == 6):
        if (team.summon == 'reached'):
            return redirect('betrayal')

    if request.method == 'POST':
        deCode = request.POST.get('decodedData')
        print(deCode)
        if (clues.id == 2 and deCode == "summon"):

            team.summon = 'reached'
            team.save()
            return JsonResponse({'redirect': '/center-game/'})
        if (clues.id == 5 and deCode == "hangman"):

            team.hangman = 'reached'
            team.save()
            return JsonResponse({'redirect': '/hangman/'})



        if (clues.id == 6 and deCode == 'betrayal' ):
            team.betrayal = 'reached'
            team.save()

            return JsonResponse({'redirect': '/bet-game/'})

        if (clues.id == 7 and deCode == "final"):
            print('rand')
            return JsonResponse({'redirect': '/final/'})

        deClue = Clue.objects.filter(code=deCode).first()
        print(deClue.id)

        if (deClue.id == (clues.id + 1)):
            print('chl')
            team.current_clue = deClue
            team.save()
            return JsonResponse({'redirect': '/clue/'})

    context = {'clue':clues}
    return render(request, 'base/clue.html', context)

@login_required(login_url='account')
def team_details(request):
    team=request.user.userprofile.team
    members= UserProfile.objects.filter(team=team)
    context={'team': team , 'members': members}
    return render(request, 'base/team_details.html',context)
@login_required(login_url='account')
def tan_exp(request):
    story=request.user.userprofile.team.storyline.name
    if (story == "story-1"):
        color="red"
    else:
        color="green"
    context={'color':color}
    return render(request, 'base/tan.html', context)

import json


@csrf_exempt
def final(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        success = data.get('success', False)  # Assuming you're sending a JSON object with a key 'success'
        if success:
            print('yay!')

    return render(request, 'base/name_game.html')
@csrf_exempt
def betrayal(request):
    teams=request.user.userprofile.team
    status=teams.status
    if (request.method=='POST'):
        if status is None:
            teams.status = 'betrayed'
            teams.save()
            next= Clue.objects.filter(id=7).first()
            teams.current_clue= next
            teams.save()
            return redirect('kataa')

        elif(status=='loyalty'):
            return redirect('loyal');

        else:
            return redirect('kataa')
    return render(request, 'base/betrayal.html')

def loyalty(request):
    teams = request.user.userprofile.team
    status = teams.status
    if status is None:
        teams.status = 'loyalty'
        teams.save()
        next = Clue.objects.filter(id=7).first()
        teams.current_clue = next
        teams.save()
        return render(request, 'base/loyalty.html')

    elif (status == 'betrayal'):
        return redirect('kataa')

    else:
        return render(request, 'base/loyalty.html')


    return render(request, 'base/loyalty.html')

@csrf_exempt
def centerGame(request):
    team = request.user.userprofile.team
    clues = team.current_clue
    newid = clues.id + 1
    newClue =Clue.objects.filter(id=newid).first()


    if (team.summon=='solved'):
        return redirect('clue')

    if (request.method=='POST'):
        deCode = request.POST.get('success')

        # Assuming you're sending a JSON object with a key 'success'
        if deCode:
            team.summon = 'solved'
            team.save()
            team.current_clue = newClue
            team.save()
            return JsonResponse({'redirect': '/clue/'})


    return render(request, 'base/center_game.html')

def betpage(request):
    teams = request.user.userprofile.team
    status = teams.status
    context = {'status':status}
    return render(request, 'base/bet-followup.html', context)
@csrf_exempt
def hangman(request):
    teams = request.user.userprofile.team
    clues = teams.current_clue
    newid = clues.id + 1
    newClue = Clue.objects.filter(id=newid).first()
    if (request.method=='POST'):
        deCode = request.POST.get('success')

        # Assuming you're sending a JSON object with a key 'success'
        if deCode:
            teams.hangman = 'solved'
            teams.save()
            teams.current_clue = newClue
            teams.save()
            return JsonResponse({'redirect': '/clue/'})
    return render(request, 'base/hangman.html')


def history(request):
    clue = request.user.userprofile.team.current_clue
    prim = clue.id

    if prim <= 7:
        clues = Clue.objects.filter(id__lt=prim)
        for clue in clues:
            print(clue.id)
    else:
        clues = Clue.objects.filter(id__gt=7, id__lt=prim)

    return render(request, 'base/history.html', {'clues': clues})

