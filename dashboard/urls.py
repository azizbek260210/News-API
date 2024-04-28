from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # --------------------------category-------------------------
    path('', views.index, name='index'),
    path('create_category/', views.create_category, name='create_category'),
    path('list_category/', views.list_category, name='list_category'),
    path('detail_category/<int:id>/', views.detail_category, name='detail_category'),
    path('edit_category/<int:id>/', views.edit_category, name = 'edit_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

    # --------------------------region-------------------------
    path('create_region/', views.create_region, name='create_region'),
    path('list_region/', views.list_region, name='list_region'),
    path('detail_region/<int:id>/', views.detail_region, name='detail_region'),
    path('edit_region/<int:id>/', views.edit_region, name = 'edit_region'),
    path('delete_region/<int:id>/', views.delete_region, name='delete_region'),

    # --------------------------post-------------------------
    path('create_post/', views.create_post, name='create_post'),
    path('list_post/', views.list_post, name='list_post'),
    path('detail_post/<int:id>/', views.detail_post, name='detail_post'),
    path('edit_post/<int:id>/', views.edit_post, name = 'edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),

    # --------------------------contact-------------------------
    path('list_contact/', views.list_contact, name='list_contact'),
    path('detail_contact/<int:id>/', views.detail_contact, name='detail_contact'),
    path('edit_contact/<int:id>/', views.edit_contact, name = 'edit_contact'),

    # -----------------register, login, logout-------------------------------
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    ]