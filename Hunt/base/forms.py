from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll_no = forms.CharField(label='Roll Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'roll-no'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone-no'}))
    branch = forms.CharField(label='Branch', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name', 'roll_no', 'email', 'phone_no', 'branch', 'password1', 'password2')


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
