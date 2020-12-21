from django.conf.urls import url
from .views import HotelView, SearchResultsView

urlpatterns = [
    url('search/', SearchResultsView.as_view(), name='search_results'),
    url('detail', HotelView.as_view(), name='detail'),
]
