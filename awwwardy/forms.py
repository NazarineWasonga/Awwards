from django import forms
from .models import *
from django.forms import ModelForm, Textarea

class NewPostForm(forms.ModelForm):
    class Meta :
        model = Projects
        exclude = ['user', 'post_date','liker']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }