from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is created Successfully')

def insert_webpage(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('Webpage is created successfully')

def insert_access(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()

    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.create(name=WO,date=d,author=a)
    AO.save()


    return HttpResponse('Webpage is created successfully')
