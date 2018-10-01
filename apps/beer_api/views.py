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
    result = beers['result']
    print("Result: {}".format(result))
    beer_list = []
    i = 0
    for i in range(0, len(result)):
        beer = result[i]
        print("Beer: {}".format(beer))
        beer_list.append(beer)
        i += 1
    context = {
        'beer_list': beer_list,
        'beers': beers,
        'result': result,
    }
    return render(request, 'beer_api/index.html', context)