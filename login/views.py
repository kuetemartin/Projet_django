from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAgents

def home(request):
    users = UserAgents.objects.all()
    return render(request,"index.html",context={
        'users':users
    })

def about(request):
    return HttpResponse('about')

def descr(request):
    return HttpResponse('descr')