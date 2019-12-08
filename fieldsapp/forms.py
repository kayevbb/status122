from .models import Post
from django import forms


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'avatar2', 'avatar3', 'avatar', 'body', 'address', 'phone_number', 'city', 'pole']