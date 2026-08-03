# pyrefly: ignore [missing-import]
from django.shortcuts import render
import datetime
from .models import Student

def index(request):
    student = Student.objects.all()
    context ={
       'title':'My Home Page',   

    }
    context['students'] = Student.objects.all().order_by('st_id')
    context['date']= datetime.date.today()
    return render(request, "index.html",context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")  
