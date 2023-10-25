from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.contrib.auth.hashers import make_password
from django.contrib.gis.db import models as model
from django.utils.translation import gettext as _

# Create your models here.


class MyUserManager(UserManager):
    """
        Creating a new user manager for our customized django user.
    """

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'admin')
        username = extra_fields['phone_number']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone_number']
        return super().create_user(username, email, password, **extra_fields)


class OrgType(models.Model):
    title = models.CharField(max_length=300, db_index=True, unique=True, verbose_name=_('organization type title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('organization type')
        verbose_name_plural = _('organizations types')


class User(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    phone_number = models.CharField(max_length=11, db_index=True, unique=True, verbose_name=_('phone number'))
    code_melli = models.CharField(max_length=10, db_index=True, unique=True, verbose_name=_('code melli'))
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        self.username = self.phone_number
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} | {self.phone_number}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Organization(models.Model):
    name = models.CharField(max_length=300, db_index=True, verbose_name=_('organization name'))
    code = models.CharField(max_length=30, unique=True, verbose_name=_('Organization code'))
    description = models.TextField(verbose_name=_('description'))
    address = models.TextField(verbose_name=_('Organization address'))
    location = model.GeometryField(geography=True, db_index=True, verbose_name=_('Location'))
    tel = models.CharField(max_length=11, verbose_name=_('tel number'), null=True, blank=True)
    o_type = models.ForeignKey(OrgType, on_delete=models.PROTECT, verbose_name=_('organization type'))
    is_active = models.BooleanField(verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def save(self, *args, **kwargs):
        if self.o_type.title == 'مشتری':
            self.is_active = True
        else:
            self.is_active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} | {self.code}'

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')


class UserGroupOrganization(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'))
    g_id = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name=_('group'))
    o_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name=_('organization'))
    ugo_code = models.IntegerField(verbose_name=_('code'), primary_key=True, unique=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def save(self, *args, **kwargs):
        code = str(self.u_id.id) + str(self.g_id.id) + str(self.o_id.id)
        code = int(code)
        self.ugo_code = code
        if self.g_id.name == 'مشتری':
            self.is_active = True
        else:
            self.is_active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.u_id} | {self.g_id} | {self.o_id}'

    class Meta:
        verbose_name = _('user group organization')
        verbose_name_plural = _('user group organization')

