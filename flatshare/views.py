from django.shortcuts import render
from django.http import HttpResponse
from flatshare.models import Flat

def index(request):
    return render(request, 'flatshare/index.html')

def about(request):
    return render(request, 'flatshare/about.html')

def login(request):
    return HttpResponse("place holder login page")

def signup(request):
    return HttpResponse("place holder signup page")

def addflat(request):
    return HttpResponse("place holder addflat page")

def findflat(request):
    return HttpResponse("place holder findflat page")

def flats(request):
    context_dict = {}

    SELECTED_ORDER = 'rent'
    flat_list = Flat.objects.order_by(SELECTED_ORDER)
    context_dict['flats'] = flat_list

    return render(request, 'flatshare/flats.html', context=context_dict)
