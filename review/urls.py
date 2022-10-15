from django.urls import path
from .apis import ReviewCreateAPI


app_name = 'review'

urlpatterns = [

    path("api/create", ReviewCreateAPI.as_view(), name="create_api"),

]
