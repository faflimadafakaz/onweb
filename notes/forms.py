'''
Created on 02-Mar-2015

@author: suraj
'''
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import TextInput, PasswordInput , Textarea
from django.utils.html import strip_tags
from notes.models import UserProfile
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, widget = TextInput(attrs={'placeholder':'username'}))
    email = forms.EmailField(required=True, widget = TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(required=True,widget = PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True,widget = PasswordInput(attrs={'placeholder':'Re-enter Password'}))
    
    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f ,error in self.errors.iteritems():
            if f!='__all__':
                self.fields[f].widget.attrs.update({'class':'error', 'value':strip_tags(error)})
        return form
    
    class Meta():
        fields = ['username','email','password1','password2']
        model = User
        
class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))
    
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f,error in self.errors.iteritems():
            if f!='__all_':
                self.fields[f].widget.attrs.update({'class':'error', 'value':strip_tags(error)})
        return form
    
# class NotesForm(forms.ModelForm):
#     title = forms.CharField(required=False, widgets=TextInput(attrs={'placeholder':'Title of note'}))
#     content = forms.CharField(required=True, widgets = Textarea(attrs={'placeholder':'Note content'}))
#     category = forms.MultiValueField()