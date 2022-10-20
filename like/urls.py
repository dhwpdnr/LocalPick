from django.urls import path
# from .apis import LikeListAPI
from .views import LikeListView

app_name = 'like'

urlpatterns = [
    # {% url 'like:list_api' %}
    # path("api/list/", LikeListAPI.as_view(), name="list_api"),
    path("list/", LikeListView.as_view(), name="list")
]
