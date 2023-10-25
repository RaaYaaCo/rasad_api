from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'code_melli', 'is_active']


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'is_active']


@admin.register(models.OrgType)
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(models.UserGroupOrganization)
class UserGroupOrganizationAdmin(admin.ModelAdmin):
    list_display = ['ugo_code', 'u_id', 'g_id', 'o_id']

