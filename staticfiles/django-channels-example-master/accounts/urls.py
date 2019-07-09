from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('not', views.new_user, name='new_use'),
]
