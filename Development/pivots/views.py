from django.shortcuts import render
from .models import staff

# Create your views here.



def index(request):
    return render(request, "pages/index.html")

def result(request):
    return render(request, "pages/result.html",{
        "staff": staff.objects.all()
    })

def form(request):
    return render(request, "pages/form.html")
