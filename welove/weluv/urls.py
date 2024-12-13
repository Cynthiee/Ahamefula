from django.urls import path 
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('middle/', views.middle, name='middle'),
    path('again/', views.again, name='again'),

]
