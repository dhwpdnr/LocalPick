from django.urls import path
from .apis import AppetiteCreateAPI
from .views import TasteCreateView


app_name = 'appetite'

urlpatterns = [
    # {% url 'appetite:create_api' %}
    path("api/create/", AppetiteCreateAPI.as_view(), name="create_api"),

    # {% url 'appetite:create' %}
    path("create/", TasteCreateView.as_view(), name="create")

]
