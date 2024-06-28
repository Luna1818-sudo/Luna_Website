from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from account.models import CustomUser
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username


        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer    
      
@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        'api/token',
        'api/token/refresh',
    ]

    return Response(routes)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username= request.data['username'] )
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    token , created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance= user)
    return Response({"token": token.key, "user": serializer.data})


    return Response({}) 


@api_view(['POST'])
def signup(request):
    serializer =UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer)
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
  
        user.save()
        token = Token.objects.create(user = user)
        return Response({"token": token.key, "user": serializer.data})
         
   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def test_token(request):
#     return Response({})
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
 
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    # user = User.objects.get(username = request.data['username'])
    # return Response("passed for {}".format(request.user.email))
    return Response("passed!")





