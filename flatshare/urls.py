from django.urls import path
from flatshare import views

app = 'flatshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]