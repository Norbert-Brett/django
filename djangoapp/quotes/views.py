from django.shortcuts import render

# Create your views here.

def index(request):
    import requests
    import json

    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,BCH,EOS,DOGE,LTC,XLM,ADA,USDT&tsyms=USD,EUR,GBP")
    price = json.loads(price_request.content)
    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'index.html', {'api': api, 'price': price})



def about(request):
    return render(request, 'about.html')