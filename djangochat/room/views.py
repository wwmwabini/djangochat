from django.shortcuts import render
from django.http import HttpResponse

def chatroom(request):
    return HttpResponse("Lets chat")