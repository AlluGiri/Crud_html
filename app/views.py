from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):

    if request.method =='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render(request,'display_topic.html',d)
    
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    if request.method =='POST':
        tn=request.POST['tn']
        to=Topic.objects.get(topic_name=tn)
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']
        WP=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
        WP.save()
        QLWO=Webpage.objects.all()
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    QTWO=Webpage.objects.all()
    d={'webpage':QTWO}
    if request.method =='POST':
        name=request.POST['n']
        wo=Webpage.objects.get(name=n)
        d=request.POST['d']
        a=request.POST['a']
        AO=Accessrecord.objects.get_or_create(name=wo,date=d,author=a)[0]
        AO.save()
        QLAO=Accessrecord.objects.all()
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)

