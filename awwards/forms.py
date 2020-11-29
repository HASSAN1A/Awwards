from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Rating,Profile
from pyuploadcare.dj.forms import ImageField

class SignUpForm(UserCreationForm):

    username = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control",
                                                               "placeholder":"Username"}))
    email = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control",
                                                               "placeholder":"Email"}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class":"form-control",
                                                               "placeholder":"Password"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={"class":"form-control",
                                                               "placeholder":"Confirm Password"}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)




class ProjectForm(forms.ModelForm):
    cover_photo = ImageField(label='')
    url = forms.URLField(label='Live site')
    widgets = {
          "title":forms.TextInput(attrs={"class":"form-control mb-4"}),
          "description":forms.Textarea(attrs={'cols': 110, 'rows': 15,"class":"form-control mb-4"}),
          "live_site":forms.URLInput(attrs={"class":"form-control mb-4"}),
          "technologies":forms.TextInput(attrs={"class":"form-control mb-4"}),
      }

    class Meta:
        model = Project
        fields = ('title','description','cover_photo', 'url','technologies')



class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']        