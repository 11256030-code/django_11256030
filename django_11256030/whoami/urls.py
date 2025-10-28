from django.urls import path
from . import views

urlpatterns = [
    path('whoamI', views.whoami, name='whoami'),
]