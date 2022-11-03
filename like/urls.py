from django.urls import path
from .apis import LikeAPI, LikeListAPI


app_name = 'like'

urlpatterns = [
    # {% url 'like:api' %}
    path("api/", LikeAPI.as_view(), name="api"),
    # {% url 'like:list_api' %}
    path("api/list/", LikeListAPI.as_view(), name="list_api")

]
