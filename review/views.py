from django.shortcuts import render
from rest_framework.views import APIView
from users.models import User

# Create your views here.


class ReviewCreateView(APIView):
    def get(self, request):

        session_user_id = request.session.get('_auth_user_id')
        user_id = User.objects.filter(id=session_user_id).first()
        if user_id is None:
            return render(request, "users/login.html")

        return render(request, "")