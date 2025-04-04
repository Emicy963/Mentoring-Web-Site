from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentees_views, name='mentees'),
    path('auth/', views.auth, name='auth_mentees'),
]

