from django.urls import path
from .apis import StoreDetailAPI, StoreListAPI
from .views import StoreCreateView


app_name = 'store'

urlpatterns = [
    #{% url 'store:detail_api' %}
    path("api/detail/<int:pk>", StoreDetailAPI.as_view(), name="detail_api"),
    path("api/list/", StoreListAPI.as_view(), name="list_api"),
    path("duffufkckaRo", StoreCreateView.as_view(), name="store_create")
]