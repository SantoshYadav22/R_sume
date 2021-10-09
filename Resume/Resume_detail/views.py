from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def run(request):
    return HttpResponse('<h1>hello it santosh</h1>')

def runs(request):
    return HttpResponse('<h1>hello it yadav</h1>')

def cores(request):
    return render(request,'base.html')
