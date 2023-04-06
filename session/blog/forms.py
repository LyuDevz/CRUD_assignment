from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.conf import settings

class BlogForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = UserCreationForm.Meta.fields + ('email',)