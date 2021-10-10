from django.urls import path
from . import views

urlpatterns = [

    path('', views.run),
    path('run/', views.runs),
    path('contact/', views.cores,name='contact'),
    path('contacts/', views.kores,name='about'),
    path('student/<int:inp>',views.student_detail),
    path('student_/',views.student_list),
    
]
 