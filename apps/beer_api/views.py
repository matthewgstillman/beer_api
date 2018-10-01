from django.shortcuts import render, redirect
from api_key import key
import requests
# Create your views here.
def index(request):
    url_root = 'https://lcboapi.com/products?access_key='
    access_key = key['api_key']
    url = str(url_root) + str(access_key)
    response = requests.get(url)
    beers = response.json()
    print("Beers: {}".format(beers))
    context = {
        'beers': beers
    }
    return render(request, 'beer_api/index.html', context)