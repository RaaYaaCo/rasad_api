from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('register-login/', views.RegisterLoginView.as_view(), name='register-login'),
    path('login/password/', views.LoginPasswordView.as_view(), name='login-password'),
    path('login/otp/', views.LoginOtpView.as_view(), name='login-otp'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='token-refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
