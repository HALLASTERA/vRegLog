from django import forms
from django.contrib.auth.models import User
from home.models import Post


class UserForm(forms.ModelForm):
    user = forms.CharField()

    class Meta:
        model = Post

