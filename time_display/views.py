from django.shortcuts import render, redirect
from time import gmtime, strftime
# Create your views here.

def index(request):
    return redirect('/time_display')

def time_display(request):
    context = {
    "hour": strftime("%H:%M %p", gmtime()),
    "date": strftime("%Y-%m-%d" ,gmtime())
    }
    return render(request,'index.html', context)