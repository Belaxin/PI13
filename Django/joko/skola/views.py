from django.shortcuts import render, HttpResponse
from .models import Student,Ucitel

def index(request):
    studenti = Student.objects.all()
    ucitelia = Ucitel.objects.all()
    return render(request, 'skola/index.html', {"studenti":studenti})