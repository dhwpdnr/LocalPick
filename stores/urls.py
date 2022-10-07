from django.urls import path
from .apis import StoreDetailAPI, StoreListAPI


app_name = 'store'

urlpatterns = [
    #{% url 'store:detail_api' %}
    path("api/detail/<int:pk>", StoreDetailAPI.as_view(), name="detail_api"),
    path("api/list/", StoreListAPI.as_view(), name="list_api")
]