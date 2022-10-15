from django.urls import path
from .apis import ReviewCreateAPI, ReviewListAPI
from .views import ReviewCreateView


app_name = 'review'

urlpatterns = [
    # {% url 'review:create_api' %}
    path("api/create", ReviewCreateAPI.as_view(), name="create_api"),
    # {% url 'review:list_api' %}
    path("api/list/<int:pk>", ReviewListAPI.as_view(), name="list_api"),


    # {% url 'review:create' %}
    path("create", ReviewCreateView.as_view(), name="create")
]
