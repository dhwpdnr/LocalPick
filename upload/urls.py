from django.urls import path
from .views import StoreUpload

app_name = 'upload'

urlpatterns = [

    path("store/", StoreUpload.as_view(), name="test"),
]