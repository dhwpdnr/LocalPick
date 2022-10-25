from django.urls import path
from .apis import StoreDetailAPI, StoreListAPI, StoreCreateAPI
from .views import StoreCreateView, StoreImageCreate, StoreDetailView, StoreListView, StoreLikeListView, StoreLike, Test


app_name = 'store'

urlpatterns = [
    # {% url 'store:detail' %}
    path("detail/<int:pk>", StoreDetailView.as_view(), name="detail"),
    # {% url 'store:detail_api' %}
    path("api/detail/<int:pk>", StoreDetailAPI.as_view(), name="detail_api"),

    # {% url 'store:list_api'%}
    path("api/list/<int:pk>", StoreListAPI.as_view(), name="list_api"),
    # {% url 'store:list' %}
    path("list/", StoreListView.as_view(), name="list"),

    # {% url 'store:create_api' %}
    path("api/create/", StoreCreateAPI.as_view(), name="create_api"),
    # {% url 'store:create_image' %}
    path("image/create/",StoreImageCreate.as_view(), name="create_image"),

    # {% url 'store:like_list' %}
    path("like/list/", StoreLikeListView.as_view(), name="like_list"),


    path("duffufkckaRo/", StoreCreateView.as_view()),


    path('like/test/', StoreLike.as_view(), name="test"),
    path('test/', Test.as_view(), name="test_page")
]