from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return HttpResponse("you are logging out")

def register(request):
    return HttpResponse("register")

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