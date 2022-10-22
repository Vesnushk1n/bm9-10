from django.shortcuts import render
from django.http import HttpResponse

def start(response):
    dat = {'data': [1,2,3,4], 'title': 'Старт'}
    return render(response, 'main/start.html', dat)

# Create your views here.
def end(response):
    return render(response, 'main/end.html')