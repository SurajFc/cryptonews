from django.shortcuts import render,redirect
from django.contrib import messages
from .models import mycontact
import requests
import json
    
    

# Create your views here.
def home(request):
 
    #Grab crypto price
    crpto_price = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,BCH,EOS,BNB.USDT,BSV,TRX&tsyms=USD").json()
    
    #Grab crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN").json()

    return render(request,"home.html",{ 'myapi': api_request, 'price':crpto_price }) 
    
def contact(request):  
    if request.method == "POST":
        fname = request.POST["fname"]
        email = request.POST["email"]
        msg = request.POST["msg"]
        myc = mycontact(fname=fname,email=email,msg=msg)
        myc.save() 
        messages.success(request,"Thank you we will contact you soon")
        return redirect("/")
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def prices(request):
    
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD").json()
        return render(request, "prices.html",{'quote':quote, 'crypto': crypto_req })
    
    else:
        notfound = "Enter a crypto currency symbol in the search bar"
        return render(request,"prices.html",{'notf':notfound}) 
    
    
def news(request): 
    api_news = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN").json()
    
    
    return render(request,"news.html",{'mynews':api_news})    