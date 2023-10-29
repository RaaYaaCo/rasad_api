from django.db import models
from user.models import UserGroupOrganization
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


class ComplaintStatus(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))

    def __str__(self):
        return self.title


class ComplaintResponse(models.Model):
    user = models.ForeignKey(UserGroupOrganization, on_delete=models.PROTECT, db_index=True, verbose_name=_('user'))
    title = models.CharField(max_length=50, db_index=True, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return f'{self.user}///{self.title}'


class Complaint(models.Model):
    user = models.ForeignKey(UserGroupOrganization, on_delete=models.PROTECT, db_index=True, verbose_name=_('user'),
                             related_name='user')
    title = models.CharField(max_length=100, db_index=True, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    store_id = models.ForeignKey(UserGroupOrganization, on_delete=models.PROTECT, verbose_name=_('store id'),
                                 related_name='store_id')
    is_read_by_admin = models.BooleanField(default=False, db_index=True, verbose_name=_('is read by admin'))
    status = models.ForeignKey(ComplaintStatus, db_index=True, on_delete=models.PROTECT,default=None,
                               verbose_name=_('status'))
    response = models.ForeignKey(ComplaintResponse, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name=_('response'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def save(self, *args, **kwargs):
        if self.user.u_id.id == self.store_id.id:
            raise ValidationError(_("User cannot file a complaint for themselves."))    
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}///{self.title}'