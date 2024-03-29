from django.contrib.auth.models import Group
from django.utils.translation import gettext as _

from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import User, UserGroupOrganization, Organization
from . import serializers
from .utils import code, get_tokens
from rasad_api import settings

# Create your views here.


class RegisterLoginView(GenericAPIView):
    serializer_class = serializers.RegisterLoginSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            user = User.objects.get(
                phone_number=serializer.data['phone_number'],
                code_melli=serializer.data['code_melli'],
            )
            if user.is_active:
                return Response({'msg': _('Login successful. The user already exists')}, status.HTTP_200_OK)
            if settings.REDIS_OTP_CODE.get(name=user.phone_number):
                return Response({'msg': _('Login successfully. Unverified user')}, status.HTTP_201_CREATED)
            else:
                otp_code = code(length=5)
                settings.REDIS_OTP_CODE.set(
                    name=user.phone_number,
                    value=otp_code,
                    ex=settings.REDIS_OTP_CODE_TIME
                )
                return Response({'msg': _('Login successfully. Unverified user'), 'code': otp_code}, status.HTTP_201_CREATED)
        except:
            try:
                user = User.objects.create(
                    phone_number=serializer.data['phone_number'],
                    code_melli=serializer.data['code_melli'],
                    is_active=False
                )
            except:
                return Response({'msg': _('The mobile number or code melli is not correct')}, status.HTTP_400_BAD_REQUEST)
            if settings.REDIS_OTP_CODE.get(name=user.phone_number):
                return Response({'msg': _('Login successfully. Unverified user')}, status.HTTP_201_CREATED)
            else:
                otp_code = code(length=5)
                settings.REDIS_OTP_CODE.set(
                    name=user.phone_number,
                    value=otp_code,
                    ex=settings.REDIS_OTP_CODE_TIME
                )
                return Response({'msg': _('New user successfully registered'), 'code': otp_code}, status.HTTP_201_CREATED)

        return Response({'msg': _('ERROR!!!')}, status.HTTP_400_BAD_REQUEST)


class LoginPasswordView(GenericAPIView):
    serializer_class = serializers.LoginPasswordSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            if serializer.data['password'] == serializer.data['password2']:
                user = User.objects.get(
                    phone_number=serializer.data['phone_number'],
                    is_active=True
                )
                if user.check_password(serializer.data['password']):
                    tokens = get_tokens(user)
                    access_token = tokens['Access']
                    refresh_token = tokens['Refresh']
                    settings.REDIS_JWT_TOKEN.set(name=refresh_token, value=refresh_token,
                                                 ex=settings.REDIS_REFRESH_TIME)

                    s_user = serializers.UserSerializer(instance=user)
                    ugo = UserGroupOrganization.objects.filter(u_id_id=user.id)
                    s_ugo = serializers.UgoSerializer(instance=ugo, many=True)

                    return Response(
                        {
                            'user': s_user.data,
                            'Organization': s_ugo.data,
                            'tokens': {'access': access_token, 'refresh': refresh_token}
                        },
                        status.HTTP_200_OK
                    )
                return Response({'msg': _('Password or confirm password is not valid')}, status.HTTP_400_BAD_REQUEST)
            return Response({'msg': _('Password or confirm password is not valid')}, status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'msg': _('Password or confirm password is not valid')}, status.HTTP_400_BAD_REQUEST)


class LoginOtpView(GenericAPIView):
    serializer_class = serializers.LoginOtpSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            user = User.objects.get(phone_number=serializer.data['phone_number'])
            otp_code = settings.REDIS_OTP_CODE.get(name=user.phone_number)
            otp_code = otp_code.decode('utf-8')
            if otp_code == serializer.data['otp_code']:
                user.is_active = True
                user.save()

                group = Group.objects.get(name='مشتری')
                group.user_set.add(user)

                organization = Organization.objects.get(code='00000')
                ugo = UserGroupOrganization.objects.create(
                    u_id=user,
                    g_id=group,
                    o_id=organization
                )

                tokens = get_tokens(user)
                access_token = tokens['Access']
                refresh_token = tokens['Refresh']
                settings.REDIS_JWT_TOKEN.set(name=refresh_token, value=refresh_token,
                                             ex=settings.REDIS_REFRESH_TIME)

                s_user = serializers.UserSerializer(instance=user)
                return Response(
                    {
                        'user': s_user.data,
                        'token': {'access': access_token, 'refresh': refresh_token}
                    },
                    status.HTTP_200_OK
                )
            return Response({'msg': _('otp code is not valid')}, status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg': _('otp code is not valid')}, status.HTTP_400_BAD_REQUEST)


class UserProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        if not instance.is_active:
            return Response({'msg': _('User not verified')})

        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)


class RefreshTokenView(GenericAPIView):
    serializer_class = serializers.RefreshTokenSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            refresh_token = settings.REDIS_JWT_TOKEN.get(name=serializer.data['refresh'])
            t_refresh = RefreshToken(refresh_token)
            user = User.objects.get(id=t_refresh['user_id'])
            settings.REDIS_JWT_TOKEN.delete(serializer.data['refresh'])
            token = get_tokens(user)
            access = token['Access']
            refresh = token['Refresh']
            settings.REDIS_JWT_TOKEN.set(name=refresh, value=refresh, ex=settings.REDIS_REFRESH_TIME)
            return Response({'access': access, 'refresh': settings.REDIS_JWT_TOKEN.get(refresh)})
        except:
            return Response({'msg': _('Token is invalid or expired')}, status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):
    serializer_class = serializers.RefreshTokenSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            settings.REDIS_JWT_TOKEN.delete(serializer.data['refresh'])
            return Response({'msg': _('logout ok')}, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token is invalid or expired'}, status.HTTP_400_BAD_REQUEST)
