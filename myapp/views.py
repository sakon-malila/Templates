# pyrefly: ignore [missing-import]
from django.shortcuts import render
import datetime
def index(request):

    context ={
       'title':'My Home Page',   

    }
    context['date']= datetime.date.today()
    return render(request, "index.html",context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")  
