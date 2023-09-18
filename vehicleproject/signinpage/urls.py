from . import views
from django.urls import path

urlpatterns = [
    path('signinpage',views.signinpage,name='signinpage')]