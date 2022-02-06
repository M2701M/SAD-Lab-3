from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

def interval(request):
	template = loader.get_template('interval.html')
	return HttpResponse(template.render())

def button(request):
    template = loader.get_template('button.html')
    return HttpResponse(template.render())

def other(request):
	template = loader.get_template('other.html')
	return HttpResponse(template.render())
