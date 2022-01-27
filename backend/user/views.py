from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .utils import get_tokens_for_user


class Login(APIView):

    def post(self, request):
        msg = dict()
        email = request.data['email']
        password = request.data['password']
        user = CustomUser.objects.filter(email=email).first()
        if user is not None:
            if user.check_password(password):
                tokens = get_tokens_for_user(user)
                access = tokens['access']
                refresh = tokens['refresh']
                msg = {
                    'refresh': refresh,
                    'access': access,
                    'state': 'login'
                }
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg['password'] = f'password is incorrect.'
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg['email'] = f'{email} is not exists.'
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
