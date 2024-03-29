from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    current_clue = models.ForeignKey('Clue', on_delete=models.SET_NULL, null=True, blank=True)
    sec_code = models.CharField(max_length=8)
    storyline = models.ForeignKey('Storyline', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    color=models.CharField(default='red', null=True, blank=True)
    # minigames = models.ManyToManyField('Minigame', related_name='teams')
    hangman= models.TextField(default = "not reached" ,null=True, blank=True)
    summon = models.TextField(default = "not reached" ,null=True, blank=True)
    betrayal=models.TextField(default = "not reached" ,null=True, blank=True)


    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,  null=True, blank=True)  # Add field for full name
    roll_no = models.CharField(max_length=9, primary_key=True)
    phone_no = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.user.username  # Change to return the full name




class Clue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField( null=True, blank=True)
    location=models.TextField( null=True, blank=True)
    hint = models.TextField( null=True, blank=True)
    # minigame = models.ForeignKey("Minigame", on_delete=models.SET_NULL, null=True, blank=True)
    code=models.CharField(max_length=10)
    storyline = models.ForeignKey('Storyline', on_delete=models.SET_NULL, null=True, blank=True)
    character=models.CharField(null=True,blank=True);

    def __str__(self):
        return self.name

class Storyline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


from django.db import models

from django.db import models


# class Betrayal(models.Model):
#     BETRAYAL_CHOICES = [
#         ('betrayed', 'Betrayed'),
#         ('loyal', 'Loyal'),
#     ]
#
#     team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name='betrayal')
#     status = models.CharField(max_length=10, choices=BETRAYAL_CHOICES, default=None, blank=True)
#
#     def __str__(self):
#         return f"{self.team.name} - {self.get_status_display()}"


# class Minigame(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
