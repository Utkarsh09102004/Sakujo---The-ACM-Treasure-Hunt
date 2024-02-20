from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', Signup, name='signups'),
    path('login/', login_view, name='logins'),
    path('team/', jcteam, name='team'),
    path('join-team/' , join_team, name='join-team'),
    path('create-team/', create_team, name='create-team'),
    path('team-details/', team_details, name='team-details'),
    path('clue/', clue_render,name='clue'),
    path('tan/', tan_exp, name='tan')

]
