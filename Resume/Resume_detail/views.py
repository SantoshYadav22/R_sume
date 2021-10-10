from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers

from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
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

#model object -single student data

def student_detail(request,inp):
    stu=Student.objects.get(id=inp)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    stu1=Student.objects.all()
    serializer1=StudentSerializer(stu1, many=True)
    json_data=JSONRenderer().render(serializer1.data)
    return HttpResponse(json_data,content_type='application/json')
