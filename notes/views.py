from django.shortcuts import render

import random

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout

from notes.forms import UserCreateForm, AuthenticateForm, CategoryForm
from notes.models import Notes, Category
from django.contrib.auth.models import User

from datetime import datetime
from django.utils.text import slugify


from django.contrib.auth.tests.test_views import LoginURLSettings
# Create your views here.

def home(request, auth_form=None, user_form=None):
    if request.user.is_authenticated():
         user = request.user
         uuser = User.objects.filter(id=user.id)[0]
         notes = Notes.objects.all().order_by('-created').filter(user=uuser)
         categories =  Category.objects.filter(user=user).order_by('name')
         category_form = CategoryForm()
         
         count = []
         
         
         return render(request, 'home.html', {'notes':notes, 'user':user, 'categories':categories, 'count':count, 'category_form':category_form})
    else:
         auth_form = auth_form or  AuthenticateForm()
         user_form =  user_form or UserCreateForm()
         return render(request, 'login.html', {'user_form':user_form, 'auth_form':auth_form}) 

def login_view(request):
    if request.method=='POST':
        if request.user.is_authenticated():
            return redirect('/')
        else:
            form = AuthenticateForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('/')
            else:
                return home(request, auth_form=form)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method=='POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return home(request, user_form=user_form)
    return redirect('home')

def add_note(request):
    if request.method=='POST':
        if request.user.is_authenticated():
            note = Notes()
            note.title = u"sample title"; 
            note.content = u"sample note content";  
            note.user = request.user;
            note.category= Category.objects.get(name='diary')
            note.created = datetime.now()
            note.permalink = unicode(slugify(note.title)+'-'+str(random.randint(1,100)))
            note.save()
        else:
            return redirect('login')
    return redirect('home')

def delete_note(request, note_slug):
    if request.method=='GET':
        if request.user.is_authenticated():
            note = Notes.objects.get(permalink = note_slug)
            note.delete()
        else:
            return redirect('login')
    return redirect('/')

def add_category(request):
    if request.user.is_authenticated():
        catform = CategoryForm(data=request.POST)
        if request.method == 'POST':
            if catform.is_valid():
                instance = catform.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            return redirect('home')
    return redirect('login')

def delete_category(request, category_slug):
    if request.method=='GET':
        if request.user.is_authenticated():
            c = Category.objects.get(slug=category_slug)
            c.delete()
        else:
            return redirect('login')
    return redirect('home')

def settings(request):
    return render(request, 'settings.html')

def uncategorized(request):
    return render(request, 'home.html')

def trash(request):
    return render(request, 'home.html')

def reminders(request):
    return render(request, 'home.html')

