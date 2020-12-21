from django.conf.urls import url
from . import views
from .views import SignUp

urlpatterns = [
    url('lk', views.lk, name='lk'),
    url('registr', views.SignUp, name='registr'),
]
