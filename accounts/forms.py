from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from app.models import Profile

def create_profile(self, **kwargs):
        Profile.objects.create(
            user=self,
            **kwargs 
        )
auth.models.User.add_to_class('create_profile', create_profile)

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=100, required = True,
    widget = forms.EmailInput())
    profile_image = forms.FileField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','profile_image')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()
        
        user.create_profile() 
        user.profile_img = self.cleaned_data.get('profile_image')
        user.profile.save()

        if commit:
            user.save()

        