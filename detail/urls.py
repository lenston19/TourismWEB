from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import HotelView, SearchResultsView

urlpatterns = [
    url('search/', SearchResultsView.as_view(), name='search_results'),
    url('detail', HotelView.as_view(), name='detail'),
]
