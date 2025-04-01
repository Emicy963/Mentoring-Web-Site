from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentees_views, name='mentees'),
]

