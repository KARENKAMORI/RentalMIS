from django.shortcuts import render
from django.http import HttpResponse
from .models import Types, Houses

# Create your views here.
def index(response, id):
    houseType = Types.objects.get(id=id)
    return render(response, "main/houses.html", {"houseType":houseType})

def home(response):
    return render(response, "main/home.html", {})

def dashboard(response):
    return HttpResponse("Tenant Dashboard")