from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

# Create your views here.
def index(req):
    return HttpResponse('placeholder to later display all the list of blogs')

def new(req):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(req):
    return redirect('/')

def show(req, number):
    numbers = number
    return HttpResponse("placeholder to display blog " + numbers)

def edit(req, number):
    new_numb = number
    return HttpResponse('placeholder to edit blog '+ new_numb)

def destory(req, number):
    return HttpResponseRedirect('/')