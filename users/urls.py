from django.urls import path
from .apis import SignupAPI, LoginAPI, UserInfoAPI
from .views import SignupView, LoginView, FindPasswordView, ChangePasswordView, TestView

app_name = 'users'

urlpatterns=[
    # {% url 'users:signup_api' %}
    path("api/signup/", SignupAPI.as_view(), name="signup_api"),
    # {% url 'users:signup' %}
    path("signup/", SignupView.as_view(),name="signup"),

    
    # {% url 'users:login_api' %}
    path("api/login/", LoginAPI.as_view(), name = "login_api"),
    # {% url 'users:login' %}
    path("login/", LoginView.as_view(), name = "login"),

    # {% url 'users:find_password' %}
    path("findpasswd/", FindPasswordView.as_view(), name="find_password"),
    path("chpasswd/", ChangePasswordView.as_view(), name="change_password"),

    # {% url 'users:info' %}
    path("user/info/<int:pk>", UserInfoAPI.as_view(), name="info"),


    path("test/", TestView.as_view(), name="test")
]



# html에서 url 사용 할때 a태그, form 태그, ajax 등(이렇게 사용해야 유지보수 편함) 
# {% url 'users:signup' %}
