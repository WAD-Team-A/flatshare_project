from django.shortcuts import render
from django.http import HttpResponse
from flatshare.models import Flat, UserProfile


def index(request):
    return render(request, 'flatshare/index.html')


def about(request):
    return render(request, 'flatshare/about.html')


def login(request):
    return HttpResponse("place holder login page")


def signup(request):
    return HttpResponse("place holder signup page")


def view_profile(request, user_slug):
    context_dict = {}
    try:
        user_profile = UserProfile.objects.get(slug=user_slug)
        context_dict['user_profile'] = user_profile
    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
    return render(request, 'flatshare/user.html', context=context_dict)


def add_flat(request):
    return HttpResponse("place holder addflat page")


def show_flat(request, flat_slug):
    context_dict = {}
    try:
        flat = Flat.objects.get(slug=flat_slug)
        context_dict['flat'] = flat
    except Flat.DoesNotExist:
        context_dict['flat'] = None
    return render(request, 'flatshare/flat.html', context=context_dict)


def list_flats(request):
    context_dict = {}

    SELECTED_ORDER = 'rent'
    flat_list = Flat.objects.order_by(SELECTED_ORDER)
    context_dict['flats'] = flat_list

    return render(request, 'flatshare/flats.html', context=context_dict)
