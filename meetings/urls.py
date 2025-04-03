from django.urls import path
from . import views

urlpatterns = [
    path('', views.meentings_view, name='meetings'),
]

