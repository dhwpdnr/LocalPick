from django.urls import path
from .apis import ReviewCreateAPI, ReviewListAPI
from .views import ReviewCreateView


app_name = 'review'

urlpatterns = [
    # {% url 'review:create_api' pk=pk %}
    path("api/create/<int:pk>", ReviewCreateAPI.as_view(), name="create_api"),
    # {% url 'review:list_api' pk=pk %}
    path("api/list/<int:pk>/", ReviewListAPI.as_view(), name="list_api"),


    # {% url 'review:create' pk=pk %}
    path("create/<int:pk>", ReviewCreateView.as_view(), name="create")
]
