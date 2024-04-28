from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('single_post', views.single_post, name='single_post'),
    path('contact/', views.contact, name='contact'),
    ]