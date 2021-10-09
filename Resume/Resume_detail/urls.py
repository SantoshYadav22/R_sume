from django.urls import path
from . import views

urlpatterns = [

    path('', views.run),
    path('run/', views.runs),
    path('contact/', views.cores,name='contact'),
    path('contacts/', views.kores,name='about'),
    
]
