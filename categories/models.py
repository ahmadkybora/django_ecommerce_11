from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(_('title'), max_length=50)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title