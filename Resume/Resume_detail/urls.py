
from django.urls import path
from . import views



urlpatterns = [

    path('', views.run),
    path('run/', views.runs),
    
]
