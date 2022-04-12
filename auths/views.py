
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, AdminSignupSerializer, ClerkSignupSerializer
from .permissions import IsAdminUser, IsClerkUser
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import User
from rest_framework .exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt, datetime



class AdminSignupView(APIView):
    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ClerkSignupView(generics.GenericAPIView):
    def post(self, request):
        serializer = ClerkSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = AdminSignupSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successfully'
        }
        return response

class AdminOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated and IsAdminUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ClerkOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated and IsClerkUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class SendEmailView(APIView):
    def post(self, request, format=None):
        data = request.data
        email = data.get('email')
        name = data.get('name')
        subject = ''
        message = ' it  means a world to us '
        res = send_mail(subject, message, settings.EMAIL_HOST_USER, [email],)

        return HttpResponse(res)
