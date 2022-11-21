from django.urls import path
from .apis import LikeAPI, LikeListAPI
from .views import StoreLikeListView
from . import views



app_name = 'like'

urlpatterns = [
    # {% url 'like:api' %}
    path("api/", views.likes, name="api"),
    # {% url 'like:list_api' %}
    path("api/list/", LikeListAPI.as_view(), name="list_api"),

    path("list/", StoreLikeListView.as_view(), name="list")
]
