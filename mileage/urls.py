from django.urls import path
from .views import *

urlpatterns = [
    path('',MainView.as_view(), name='main'),
    path('signup',SignupView.as_view(), name='signup'),
    path('signup_result',RegisterAccount.as_view(),name='signup_result'),
    path('login',LoginView.as_view(), name='login'),
    path('login_validate',LoginValidateView.as_view(),name='login_validate'),
    path('register_mileage',RegisterMileageView.as_view(),name='register_mileage'),
    path('mileage_history',MileageHistoryView.as_view(), name='list'),
]