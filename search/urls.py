from django.urls import path
from .views import SearchView, SearchResultView
from .apis import SearchAPI


app_name = 'search'

urlpatterns = [

    path("", SearchView.as_view(), name="search"),
    path("result/", SearchResultView.as_view(), name="result"),

    path("api/result/<str:search_word>", SearchAPI.as_view(), name="result_api")

]