from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def run(request):
    return HttpResponse('<h1>hello it santosh</h1>')

def runs(request):
    return render(request,'corehtml/base.html')

def cores(request):
    return render(request,'corehtml/about.html')

def kores(request):
    return render(request,'corehtml/contact.html')
