from django.http import HttpResponse
from django.shortcuts import render


def homepage(req):
    # return HttpResponse("home")
    return render(req, 'homepage.html')


def about(req):
    # return HttpResponse("about")
    return render(req, 'about.html')
