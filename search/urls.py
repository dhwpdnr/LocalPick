from django.urls import path
from .views import SearchView, SearchResultView
from .apis import SearchAPI


app_name = 'search'

urlpatterns = [
    # {% url 'search:search' %}
    path("", SearchView.as_view(), name="search"),
    # path("result/", SearchResultView.as_view(), name="result"),

    # {% url 'search:result_api' %}
    path("api/result/", SearchAPI.as_view(), name="result_api")
]