from django.urls import path
from flatshare import views

app_name = 'flatshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('flats/', views.list_flats, name="list_flats"),
    path('flats/<slug:flat_slug>/', views.show_flat, name='show_flat'),
    path('flats/<slug:flat_slug>/like/', views.like_flat, name='like_flat'),
    path('users/<slug:user_slug>/', views.view_profile, name='view_profile'),
    path('users/<slug:user_slug>/change_password/', views.change_password, name='change_password'),
    path('my_matches/', views.my_matches, name='my_matches'),
    path('my_matches/<slug:user_slug>/like/', views.like_profile, name='my_matches'),
    path('my_matches/<slug:flat_slug>/unlike/', views.unlike_flat, name='unlike_flat'),
    path('add_flat/', views.add_flat, name='add_flat'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
