from django.urls import path
from .apis import AppetiteCreateAPI


app_name = 'appetite'

urlpatterns = [

    path("api/create", AppetiteCreateAPI.as_view(), name="create_api"),

]
