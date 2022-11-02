from django.urls import path
from .apis import LikeAPI


app_name = 'like'

urlpatterns = [
    # {% url 'like:api' %}
    path("api/", LikeAPI.as_view(), name="api"),

]
