from django.conf.urls import url
from . import views
from .views import lk

urlpatterns = [
    url('lk', lk.as_view(), name='lk'),
    url('registr', views.SignUp, name='registr'),
]
