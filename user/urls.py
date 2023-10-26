from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('register-login/', views.RegisterLoginView.as_view(), name='register-login'),
    path('login/password/', views.LoginPasswordView.as_view(), name='login-password'),
]
