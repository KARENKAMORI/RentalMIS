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

def search_house(request):
    if request.method == "POST":
        searched = request.POST['searched']
        house = Houses.objects.filter(location__contains=searched)
        return render(request, "main/houseSearch.html", {"searched":searched, 'house':house})
    else:
        return render(request, "main/houseSearch.html", {})