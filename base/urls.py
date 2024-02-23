from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', team_details, name='team-details'),
    path('account/', account_view, name='account'),
    path('signup/', Signup, name='signups'),
    path('login/', login_view, name='logins'),
    path('team/', jcteam, name='team'),
    path('join-team/' , join_team, name='join-team'),
    path('create-team/', create_team, name='create-team'),
    path('clue/', clue_render, name='clue'),
    path('tan/', tan_exp, name='tan'),
    path('final/', final, name='final'),
    path('bet-game/', betrayal, name='betrayal'),
    path('bet-followup/', betpage,name='kataa'),
    path('center-game/', centerGame , name='center-game'),
    path('hangman/', hangman, name='hangman'),
    path('history/', history, name='history')

]
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
