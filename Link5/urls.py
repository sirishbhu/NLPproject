from django.urls import path
from Link5 import views

urlpatterns = [
    path('', views.Link5, name='Link5'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload/', views.upload, name='upload'),
]
