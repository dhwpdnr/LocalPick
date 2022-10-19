from django.urls import path
from .apis import LikeListAPI

app_name = 'like'

urlpatterns = [
    path("api/list/", LikeListAPI.as_view(), name="list_api"),
]
