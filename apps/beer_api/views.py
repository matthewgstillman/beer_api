from django.shortcuts import render, redirect
from api_key import key
import requests
# import mathfilters
# Create your views here.

def datasets(request):
    url_root = 'https://lcboapi.com/datasets?access_key='
    access_key = key['api_key']
    url = str(url_root) + str(access_key)
    response = requests.get(url)
    datasets = response.json()
    print("Datasets: {}".format(datasets))
    result = datasets['result']
    print("Result: {}".format(result))
    dataset_list = []
    i = 0
    for i in range(0, len(result)):
        data = result[i]
        print("Data: {}".format(data))
        dataset_list.append(data)
        i += 1
    # print("Dataset List: {}".format(dataset_list))
    context = {
        'dataset_list': dataset_list,
        'result': result,
    }
    return render(request, 'beer_api/datasets.html', context)

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

def inventories(request):
    url_root = 'https://lcboapi.com/products?access_key='
    access_key = key['api_key']
    url = str(url_root) + str(access_key)
    response = requests.get(url)
    inventories = response.json()
    print("Inventories: {}".format(inventories))
    result = inventories['result']
    print("Result: {}".format(result))
    inventory_list = []
    i = 0
    for i in range(0, len(result)):
        inventory = result[i]
        print("Inventory: {}".format(inventory))
        inventory_list.append(inventory)
        i += 1
    context = {
        'inventories': inventories,
        'inventory_list': inventory_list,
        'result': result,
    }
    return render(request, 'beer_api/inventories.html', context)

def stores(request):
    url_root = 'https://lcboapi.com/stores?access_key='
    access_key = key['api_key']
    url = str(url_root) + str(access_key)
    response = requests.get(url)
    stores = response.json()
    print("Stores: {}".format(stores))
    result = stores['result']
    print("Result: {}".format(result))
    store_list = []
    i = 0
    for i in range(0, len(result)):
        store = result[i]
        print("Store: {}".format(store))
        store_list.append(store)
        i += 1
    context = {
        'stores': stores,
        'store_list': store_list,
        'result': result,
    }
    return render(request, 'beer_api/stores.html', context)