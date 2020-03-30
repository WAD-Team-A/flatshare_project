from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from flatshare.models import Flat, UserProfile, Address
from flatshare.forms import AddFlatForm, UserProfileForm, UserForm, AddAddressForm
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse



def index(request):
    return render(request, 'flatshare/index.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user :
            if user.is_active:
                login(request, user)
                return redirect(reverse('flatshare:index'))
            else:
                return HttpResponse('Your flatshare account is disabled')
        else:
            print(f"invalid login details: {username}, {password}")
            return HttpResponse("invalid login details uspplied")
    else:
        return render(request, 'flatshare/login.html')


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return redirect(reverse('flatshare:index'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'flatshare/signup.html',context = {'user_form': user_form,'profile_form': profile_form,'registered': registered})



def view_profile(request, user_slug):
    context_dict = {}
    try:
        user_profile = UserProfile.objects.get(slug=user_slug)
        context_dict['user_profile'] = user_profile
    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
    return render(request, 'flatshare/user.html', context=context_dict)


def add_flat(request):
    address_form = AddAddressForm()
    form = AddFlatForm()

    if request.method == 'POST':
        address_form = AddAddressForm(request.POST)
        form = AddFlatForm(request.POST)

        if all((address_form.is_valid(), form.is_valid())):
            address = address_form.save(commit=True)
            print(address)
            flat = form.save(commit=False)
            print(flat)
            flat.address = address
            flat.save()
            return redirect('/')
        else:
            print('YIKES')
            print(address_form.errors)
            print(form.errors)
    return render(request, 'flatshare/add_flat.html', {'address_form': address_form, 'form': form,})


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
