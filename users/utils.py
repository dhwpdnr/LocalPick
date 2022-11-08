from users.models import User
from rest_framework.authtoken.models import Token


def user_session_authticate(request):
    phone_number = request.session.get("phone_number", None)
    user = User.objects.filter(phone_number=phone_number).first()
    if user is None:
        return None
    token = Token.objects.filter(user=user).first()

    user_info = {
        "user": user,
        "token": token.key,
    }

    return user_info