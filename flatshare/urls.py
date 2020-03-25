from django.urls import path
from flatshare import views

app_name = 'flatshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('flats/', views.list_flats, name="list_flats"),
    path('flats/<slug:flat_slug>/', views.show_flat, name='show_flat'),
    path('users/<slug:user_slug>', views.view_profile, name='view_profile'),
    path('add_flat/', views.add_flat, name='add_flat'),
]
