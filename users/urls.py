from django.urls import path
from .apis import SignupAPI, LoginAPI, UserInfoAPI, PhoneValidateAPI, NicknameValidateAPI, WithdrawalAPI
from .views import SignupView, LoginView, FindPasswordView, ChangePasswordView, TestView, MypageView, Logout

app_name = 'users'

urlpatterns=[
    # {% url 'users:signup_api' %}
    path("api/signup/", SignupAPI.as_view(), name="signup_api"),
    # {% url 'users:signup' %}
    path("signup/", TestView.as_view(),name="signup"),

    
    # {% url 'users:login_api' %}
    path("api/login/", LoginAPI.as_view(), name = "login_api"),
    # {% url 'users:login' %}
    path("login/", LoginView.as_view(), name = "login"),

    # {% url 'users:find_password' %}
    path("findpasswd/", FindPasswordView.as_view(), name="find_password"),
    # {% url 'users:change_password' %}
    path("chpasswd/", ChangePasswordView.as_view(), name="change_password"),

    # {% url 'users:info_api' %}
    path("user/info/<int:pk>", UserInfoAPI.as_view(), name="info_api"),

    # {% url 'users:mypage' %}
    path("my/", MypageView.as_view(), name="mypage"),

    # {% url 'users:phone_check' %}
    path("phone/check/", PhoneValidateAPI.as_view(), name="phone_check"),
    # {% url 'users:nickname_check' %}
    path("nickname/check/", NicknameValidateAPI.as_view(), name="nickname_check"),

    # {% url 'users:logout' %}
    path("logout/", Logout.as_view(),name="logout"),
    # {% url 'users:withdrawal' %}
    path("withdrawal/<int:pk>", WithdrawalAPI.as_view(), name="withdrawal"),


    path("test/", TestView.as_view(), name="test"),
]



# html에서 url 사용 할때 a태그, form 태그, ajax 등(이렇게 사용해야 유지보수 편함) 
# {% url 'users:signup' %}
