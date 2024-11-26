from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def btc(request):
    return HttpResponse('<h1>btccoin is number 1 crypto and it is reach 100k dolers resently</h1>')