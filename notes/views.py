from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout

from notes.forms import UserCreateForm, AuthenticateForm
from notes.models import Notes, Category
from django.contrib.auth.models import User
# Create your views here.

def home(request, auth_form=None, user_form=None):
    if request.user.is_authenticated():
         user = request.user            
         uuser = User.objects.filter(id=user.id)[0]
        
         notes = Notes.objects.all().order_by('-created').filter(user=uuser)
         categories=  Category.objects.all()
         return render(request, 'home.html', {'notes':notes, 'user':user, 'categories':categories})
    else:
         auth_form = auth_form or  AuthenticateForm()
         user_form =  user_form or UserCreateForm()
         return render(request, 'login.html', {'user_form':user_form, 'auth_form':auth_form}) 

def login_view(request):
    if request.method=='POST':
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
            return redirect('/')
        else:
            return home(request, user_form=user_form)
    return redirect('/')

def add_note(request, note_slug):
    return HttpResponse("adding note"+ note_slug)

def delete_note(request, note_slug):
    return HttpResponse('delete note'+ note_slug)

def settings(request):
    return render(request, 'settings.html')

def uncategorized(request):
    return render(request, 'home.html')

def trash(request):
    return render(request, 'home.html')

def reminders(request):
    return render(request, 'home.html')