from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home-view'),
    path('sync/', views.main_view, name='sync-main-view'),
    path('async/', views.main_view_async, name='async-main-view'),

]