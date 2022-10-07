from django.urls import path
from .apis import SignupAPI, LoginAPI
from .views import SignupView, LoginView

app_name = 'users'

urlpatterns=[
    #{% url 'users:signup_api' %}
    path("api/signup/", SignupAPI.as_view(), name="signup_api"),
    #https://localpick-ycqet.run.goorm.io/auth/signup/
    #{% url 'users:signup' %}
    path("signup/", SignupView.as_view(),name="signup"),

    
    #{% url 'users:login_api' %}
    path("api/login/", LoginAPI.as_view(), name = "login_api"),
    #https://localpick-ycqet.run.goorm.io/auth/login/
    #{% url 'users:login' %}
    path("login/", LoginView.as_view(), name = "login")
]



# html에서 url 사용 할때 a태그, form 태그, ajax 등(이렇게 사용해야 유지보수 편함) 
# {% url 'users:signup' %}
