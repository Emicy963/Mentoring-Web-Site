from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_view, name='meetings'),
    path('choose_day', views.choose_day, name='choose_day'),
]

