from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def doge(request):
    return HttpResponse('<h1>dogecoin is number 3 crypto and it is 0.45$</h1>')