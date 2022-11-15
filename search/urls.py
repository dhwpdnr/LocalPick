from django.urls import path
from .views import SearchView, SearchResultView
from .apis import SearchAPI


app_name = 'search'

urlpatterns = [
    # {% url 'search:search' %}
    path("", SearchView.as_view(), name="search"),
    path("result/<str:search_word>", SearchResultView.as_view(), name="result"),

    # {% url 'search:result_api' %}
    path("api/result/<str:search_word>", SearchAPI.as_view(), name="result_api")
]