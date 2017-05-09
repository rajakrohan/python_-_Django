 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Album
from django.http import  Http404
from django.template import loader

from django.shortcuts import render

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {
       'all_albums': all_albums,
    }
    #html=''
    #for album in all_albums:
           #html+='<a href="' + url +'">' + album.album_title + '</a><br>'
    #return HttpResponse(template.render(context, request))
    return render(request,'music/index.html',context)
    #return HttpResponse(html)

def detail(request, album_id):
    #return HttpResponse("<h2> Details for Album id: " + str(album_id) + "</h2>")
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("ALBUM DOES NOT EXSISTS")
    return render(request,'music/detail.html',{'album':album})