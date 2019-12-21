from django.shortcuts import render
from myapp.models import Songs
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def songs(request):
    return HttpResponse(Songs.objects.values())

def getsong(request,id):
    return HttpResponse(Songs.objects.get(id=id))

@csrf_exempt
def saveSong(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        song = Songs()
        song.name = body['name']
        song.track = body['track']
        song.length = body['length']
        song.save()
    return HttpResponse('saved')


@csrf_exempt
def updateSong(request,id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        song = Songs.objects.get(id = id)
        song.track = body['track']
        song.save()
    return HttpResponse('updated')