from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class ZipUpload(models.Model):
    class Meta:
        app_label = 'cms'
        verbose_name = _('Zip Upload')
        verbose_name_plural = _('Zip Upload')




