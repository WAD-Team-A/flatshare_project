from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from flatshare.models import Flat, UserProfile, Match
from flatshare.forms import AddFlatForm, UserProfileForm, UserForm, AddAddressForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'flatshare/index.html')


def about(request):
    context_dict = {}
    if request.user.is_authenticated:
        context_dict["user_authenticated"] = True
        user = UserProfile.objects.get(user=request.user)
        context_dict['user'] = user
    return render(request, 'flatshare/about.html', context=context_dict)


def contact(request):
    context_dict = {}
    if request.user.is_authenticated:
        context_dict["user_authenticated"] = True
        user = UserProfile.objects.get(user=request.user)
        context_dict['user'] = user
    return render(request, 'flatshare/contact.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('flatshare:index'))
            else:
                return HttpResponse('Your flatshare account is disabled')
        else:
            print(f"invalid login details: {username}, {password}".format(username=username, password=password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'flatshare/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('flatshare:index'))


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
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'], )
            login(request, user)
            return redirect(reverse('flatshare:index'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'flatshare/signup.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required()
def change_password(request, user_slug):
    u = request.user
    errors = None
    password_form = ChangePasswordForm(request.POST)
    if password_form.is_valid() and u.check_password(password_form.cleaned_data['password']):
        u.set_password(password_form.cleaned_data['new_password'])
        u.save()
        redirect(reverse('flatshare:login'))
    else:
        errors = password_form.errors
    return render(request, 'flatshare/change_password.html', context={'user': request.user, 'password_form' : password_form, 'errors': errors})


@login_required()
def view_profile(request, user_slug):
    context_dict = {}
    try:
        user = User.objects.get(username=user_slug)
        user_profile = UserProfile.objects.get(user=user)
        context_dict['user_profile'] = user_profile
        context_dict['owned_flats'] = user_profile.user.owned_flat_set.all()
    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
    return render(request, 'flatshare/user.html', context=context_dict)


@login_required()
def like_profile(request, user_slug):
    liked_user = UserProfile.objects.get(slug=user_slug)
    if liked_user not in request.user.userprofile.liked_users.all():
        request.user.userprofile.liked_users.add(liked_user.user)
        Match.objects.create(m_user=liked_user, m_flat=liked_user.liked_flats.get(owner=request.user),
                             m_owner=request.user.userprofile)
    return redirect(reverse('flatshare:my_matches'))


@login_required
def my_matches(request):
    context_dict = {}
    flat_matches = []
    try:
        context_dict["likes"] = request.user.userprofile.liked_flats.all()
        for match in Match.objects.filter(m_user=request.user.userprofile).all():
            flat_matches.append(match)
        for match in Match.objects.filter(m_owner=request.user.userprofile).all():
            flat_matches.append(match)
        context_dict['matches'] = flat_matches
        flat_likers = Flat.objects.get(owner=request.user).likers.all()
        context_dict['likers'] = flat_likers
    except Flat.DoesNotExist:
        pass
    return render(request, 'flatshare/matches.html', context=context_dict)


@login_required()
def add_flat(request):
    if request.user.is_authenticated:
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
                flat.owner = request.user
                flat.save()
                return redirect('/')
            else:
                print('YIKES')
                print(address_form.errors)
                print(form.errors)
        return render(request, 'flatshare/add_flat.html', {'address_form': address_form, 'form': form, })
    else:
        return HttpResponse("please log in first!")


def show_flat(request, flat_slug):
    context_dict = {}
    try:
        flat = Flat.objects.get(slug=flat_slug)
        context_dict['flat'] = flat
    except Flat.DoesNotExist:
        context_dict['flat'] = None
    return render(request, 'flatshare/flat.html', context=context_dict)


@login_required()
def like_flat(request, flat_slug):
    liked_flat = Flat.objects.get(slug=flat_slug)
    if liked_flat not in request.user.userprofile.liked_flats.all() and liked_flat not in request.user.owned_flat_set.all():
        request.user.userprofile.liked_flats.add(liked_flat)
    return redirect(reverse('flatshare:show_flat', args=[liked_flat.slug]))


@login_required()
def unlike_flat(request, flat_slug):
    unliked_flat = Flat.objects.get(slug=flat_slug)
    if unliked_flat in request.user.userprofile.liked_flats.all() and unliked_flat not in request.user.owned_flat_set.all():
        request.user.userprofile.liked_flats.remove(unliked_flat)
    return redirect(reverse('flatshare:my_matches'))


def list_flats(request):
    context_dict = {}
    SELECTED_ORDER = 'rent'
    flat_list = Flat.objects.order_by(SELECTED_ORDER)
    context_dict['flats'] = flat_list

    return render(request, 'flatshare/flats.html', context=context_dict)
