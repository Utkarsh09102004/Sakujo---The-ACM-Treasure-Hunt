from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    roll_no = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15)
    branch = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('name', 'roll_no', 'email', 'phone_no', 'branch', 'password1')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['roll_no']  # Assign roll_no as username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                roll_no=self.cleaned_data['roll_no'],
                phone_no=self.cleaned_data['phone_no'],
                branch=self.cleaned_data['branch']
            )
        return user
