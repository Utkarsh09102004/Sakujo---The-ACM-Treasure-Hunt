from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .algos import *
from .models import *
from django.http import JsonResponse
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

def jcteam(request):
    return render(request, 'base/team.html')

def create_team(request):
    sec_code=generate_random_string(8)
    users=request.user.userprofile

    if request.method == 'POST':
        team_name = request.POST.get('teamName')
        print(team_name)
        team = Team.objects.create(name=team_name, sec_code=sec_code)
        users.team = team
        users.save()
        return redirect('team-details')


    context={'sec_code':sec_code}
    return render(request, 'base/create_team.html',context)

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Team

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

def clue_render(request):
    team =request.user.userprofile.team
    clues=team.current_clue
    print(clues.id)

    if request.method == 'POST':
        deCode = request.POST.get('decodedData')
        print(deCode)
        deClue = Clue.objects.filter(code=deCode).first()
        print(deClue.id)
        if (deClue.id == (clues.id + 1)):
            print('chl')
            team.current_clue = deClue
            team.save()
            return JsonResponse({'redirect': '/clue/'})

    context = {'clue':clues}
    return render(request, 'base/clue.html', context)
def team_details(request):
    team=request.user.userprofile.team
    members= UserProfile.objects.filter(team=team)
    context={'team': team , 'members': members}
    return render(request, 'base/team_details.html',context)

def tan_exp(request):
    story=request.user.userprofile.team.storyline.name

    if (story == "story-1"):
        color="red"
    else:
        color="green"

    context={'color':color}

    return render(request, 'base/tan.html', context)