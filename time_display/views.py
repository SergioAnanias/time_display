from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "hour": strftime("%H:%M %p", gmtime()),
        "date": strftime("%Y-%m-%d" ,gmtime())
    }
    return render(request,'index.html', context)