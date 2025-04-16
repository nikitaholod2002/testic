from django import forms
from django.db import models
from .models import Post

class PostForm(forms.Form):

    name = forms.CharField(label="Название",max_length=100)
    full_text = forms.CharField(label='Описание', widget=forms.Textarea)

   
    class Meta:
        model = Post
        fields = ('name', 'full_text')
