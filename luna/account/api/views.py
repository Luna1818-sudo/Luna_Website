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
from django.shortcuts import HttpResponse
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


@api_view(['GET'])
def login(request, username, format = None):
    user = get_object_or_404(User, username = username )

    # if not user.is_active:
    #     return Response({"detail": "User account is not active."}, status=status.HTTP_400_BAD_REQUEST)
    # if not user.check_password(request.data['password']):
    #     return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    # token , created = Token.objects.get_or_create(user=user)
    # serializer = UserSerializer(instance= user)
    # return Response({"token": token.key, "user": serializer.data})
    return HttpResponse(f'{username}')


    return Response({}) 


@api_view(['GET','POST'])
def signup(request):
    serializer =UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer)
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.is_active = True
  
        user.save()
        token = Token.objects.create(user = user)
        
        response_data = {
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
        
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


@api_view(['GET'])
def account_view(request):

    if request.method == 'GET':
        all_accounts = User.objects.all()
        account_serializer = UserSerializer(all_accounts, many=True)
        return Response(account_serializer.data)
    
@api_view(['GET'])
def account_detail(request, username, format = None):

    account_detail_view = User.objects.get(username= username)
    if request.method == "GET":
        account_specific_serializer = UserSerializer(account_detail_view)
        return Response(account_specific_serializer.data)
     
        






