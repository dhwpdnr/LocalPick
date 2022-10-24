from django.urls import path
from .views import SearchView, SearchResultView


app_name = 'search'

urlpatterns = [

    path("", SearchView.as_view(), name="search"),
    path("result/", SearchResultView.as_view(), name="result")

]