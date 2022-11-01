from django.urls import path
from .apis import AppetiteCreateAPI


app_name = 'like'

urlpatterns = [
    # {% url 'like:api' %}
    path("api/", AppetiteCreateAPI.as_view(), name="api"),

]
