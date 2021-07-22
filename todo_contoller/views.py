from django.shortcuts import render

# Create your views here.
from .models import Student,User
from .serializers import StudentSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User Not Found")
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")

        #Creating jwt token
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,"SECRET",algorithm='HS256')
        jwt.decode(token,'SECRET',algorithms=['HS256'])
        
        response = Response()
        #when we want to send jwt creddentials to 
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated User")

        try:
            payload = jwt.decode(token,'SECRET',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!!!")
        user= User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'logged out'
        }
        return response

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # {"email":"namanjaiswal.53@gmail.com",
    # "password":"Movies@123"}