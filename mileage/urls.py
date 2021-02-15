from django.urls import path
from .views import *

urlpatterns = [
    path('',LoginView.as_view(), name='login'),
    path('signup',SignupView.as_view(), name='signup'),
    path('signup_result',RegisterAccount.as_view(),name='signup_result'),
    path('login',LoginView.as_view(), name='login'),
    path('login_result',LoginResultView.as_view(),name='login_result'),
    path('register_mileage',RegisterMileageView.as_view(),name='register_mileage'),
]