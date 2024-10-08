from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from django.urls import re_path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/<str:username>',views.login),
    re_path('signup',views.signup),
    re_path('test_token',views.test_token),
    path('accounts/', views.account_view),
    path('accountsearch/<str:username>', views.account_detail),

]