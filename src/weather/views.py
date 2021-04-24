from django.shortcuts import render
from decouple import config
import requests

def index(request):
    url = config("BASE_URL")
    city = "Berlin"
    r = requests.get(url.format(city))
    a = r.json()
    return render(request, "weather/index.html")
