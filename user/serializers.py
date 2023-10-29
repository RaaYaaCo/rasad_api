from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import User, Organization, OrgType, UserGroupOrganization
from .validators import check_phone, isnumeric


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'code_melli', 'groups']


class OrgTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgType
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    o_type = OrgTypeSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = ['id', 'name', 'code', 'description', 'address', 'location', 'tel', 'o_type', 'is_active', 'created_at']


class UgoSerializer(serializers.ModelSerializer):
    u_id = UserSerializer(read_only=True)
    g_id = GroupSerializer(read_only=True)
    o_id = OrganizationSerializer(read_only=True)

    class Meta:
        model = UserGroupOrganization
        fields = ['ugo_code', 'u_id', 'g_id', 'o_id', 'created_at']


class RegisterLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, validators=[check_phone])
    code_melli = serializers.CharField(required=True, min_length=10, validators=[isnumeric])


class LoginPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, required=True)
    password2 = serializers.CharField(min_length=8, required=True)


class LoginOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    otp_code = serializers.IntegerField(required=True, min_value=5, max_value=5)


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True, label=_('password'))
    password2 = serializers.CharField(min_length=8, required=True, write_only=True, label=_('confirm password'))
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'code_melli',
            'password',
            'password2',
            'groups',
            'is_active',
        ]
        read_only_fields = ['id', 'phone_number', 'code_melli', 'groups', 'is_active']

        def update(self, validated_data):
            user = User.objects.update(
                id=validated_data['id'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
            )

            return user

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise ValidationError(_('The passwords must match'))
        return data


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=1500, required=True, label=_('refresh'))
