from django.shortcuts import render

# Create your views here.
def core(request):
    return render (request,'corehtml/base.html',{'hello':'string'})