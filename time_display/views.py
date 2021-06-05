from django.shortcuts import render, redirect
from time import gmtime, strftime, localtime
# Create your views here.

def index(request):
    return redirect('/time_display')

def time_display(request):
    date_time = localtime()
    context = {
    "hour": date_time.tm_hour,
    "min": date_time.tm_min,
    "sec": date_time.tm_sec,
    "day": date_time.tm_mday,
    "month": date_time.tm_mon,
    "year": date_time.tm_year
    }
    return render(request,'index.html', context)