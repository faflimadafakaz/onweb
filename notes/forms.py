'''
Created on 02-Mar-2015

@author: suraj
'''
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import TextInput, PasswordInput , Textarea,\
    ChoiceInput
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.forms.models import ModelForm


from notes.models import Category, Notes

class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, widget = TextInput(attrs={'placeholder':'username', 'class':'form-control'}))
    email = forms.EmailField(required=True, widget = TextInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password1 = forms.CharField(required=True,widget = PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))
    password2 = forms.CharField(required=True,widget = PasswordInput(attrs={'placeholder':'Re-enter Password', 'class':'form-control'}))
    
    class Meta():
        fields = ['username','email','password1','password2']
        model = User
        
class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder':'username', 'class':'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password', 'class':'form-control'}))
    
    
class NotesForm(forms.ModelForm):
     title = forms.CharField(required=False, widget=TextInput(attrs={'placeholder':'Title of note','class':"form-control"}))
     content = forms.CharField(required=True, widget = Textarea(attrs={'placeholder':'Note content','class':"form-control"}))
     category = forms.ModelChoiceField(label="Category", queryset=Category.objects.filter(user=Category.objects.all()))
     
     def __init__(self, user, *args, **kwargs):
         super(NotesForm, self).__init__(*args, **kwargs)
         if user:
             qs = Category.objects.filter(user=user)
             self.fields['category'] = forms.ModelChoiceField(label='', queryset= qs)
         
     
     class Meta:
         model=Notes
         fields = ['title', 'content','category']
         


class CategoryForm(ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={'placeholder':'new category', 'class':"form-control", 'id':'form70pc'}))
    
    class Meta:
        model=Category
        fields = ['name']
        