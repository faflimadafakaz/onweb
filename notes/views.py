from django.shortcuts import render
import hashlib
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from notes.forms import UserCreateForm, AuthenticateForm, CategoryForm, NotesForm
from notes.models import Notes, Category
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.tests.test_views import LoginURLSettings
# Create your views here.

def home(request, auth_form=None, user_form=None, notes_form=None, category_form=None, message=None):
    message=''
    if request.user.is_authenticated():
        if request.method=='POST':
            catform = CategoryForm(data=request.POST)
            noteform = NotesForm(user=request.user, data=request.POST)
            
            if catform.is_valid():
                name = catform.cleaned_data
                if not Category.objects.filter(user=request.user, name=name['name']):
                    instance = catform.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    message = "Category "+ name['name']+ " added"
                else:
                    message="Duplicate category name"
                    
            
            if noteform.is_valid():
                instance = noteform.save(commit=False)
                instance.user = request.user
                cat = instance.category
                instance.category = Category.objects.get(user=request.user, name=cat)
                a = datetime.now()
                a =  str(a.second + a.minute+a.hour+a.day+a.month+a.year)+str(request.user)
                m = hashlib.new('ripemd160')
                m.update(a)
                instance.permalink=m.hexdigest()
                instance.save()
                message="Note added"
            
        
        user = request.user
        notes = Notes.objects.all().order_by('-created').filter(user=user)
        if not notes:
            message="No notes here"
        categories =  Category.objects.filter(user=user).order_by('name')
        category_form = category_form or CategoryForm()
        notes_form = notes_form or NotesForm(user)
        count={}
        for cat in categories:
            count[cat]=0
            
        for note in notes:
            count[note.category]+=1
        
        
        return render(request, 'home.html', {'notes':notes, 'user':user, 'categories':categories, 'count':count, 'category_form':category_form,'message':message,'notes_form':notes_form})
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

def edit_note(request, note_slug):
    if request.user.is_authenticated():
        note = Notes.objects.get(user=request.user, slug=note_slug)
        return render(request, 'edit_note.html', {note:note})
    return redirect('/')
def delete_note(request, note_slug):
    if request.method=='GET':
        if request.user.is_authenticated():
            note = Notes.objects.get(permalink = note_slug)
            note.delete()
        else:
            return redirect('login')
    return redirect('/')

def delete_category(request, category_slug):
    if request.user.is_authenticated():
        if request.method=='GET':   
            c = Category.objects.get(slug=category_slug, user=request.user)
            c.delete()
        else:
            return redirect('home')
    return redirect('login')

def settings(request):
    return render(request, 'settings.html')

def uncategorized(request):
    return render(request, 'home.html')

def trash(request):
    return render(request, 'home.html')

def reminders(request):
    return render(request, 'home.html')

def notes_by_category(request, category_slug):
    if request.user.is_authenticated():
        user = request.user
        categories = Category.objects.filter(user=user)
        count=0
        category_form = CategoryForm()
        cat = Category.objects.get(user=user, slug=category_slug)
        notes = Notes.objects.filter(category = cat).order_by('-created')
        return render(request, 'home.html',{'notes':notes, 'user':user, 'categories':categories, 'count':count, 'category_form':category_form})
    else:
        return render('login')