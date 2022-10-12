from django.urls import path
from .apis import StoreDetailAPI, StoreListAPI, StoreCreateAPI
from .views import StoreCreateView, StoreImageCreate, StoreDetailView, StoreListView


app_name = 'store'

urlpatterns = [

    path("detail/<int:pk>", StoreDetailView.as_view(), name="detail"),
    # {% url 'store:detail_api' %}
    path("api/detail/<int:pk>", StoreDetailAPI.as_view(), name="detail_api"),

    # {% url 'store:list_api'%}
    path("api/list/", StoreListAPI.as_view(), name="list_api"),
    path("list/", StoreListView.as_view(), name="list"),

    # {% url 'store:create_api' %}
    path("api/create/", StoreCreateAPI.as_view(), name="create_api"),
    path("image/create/",StoreImageCreate.as_view(), name="create_image"),

    path("duffufkckaRo/", StoreCreateView.as_view())
]