from django.db import models
from django.utils.translation import gettext_lazy as _
from categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='%(class)s', on_delete=models.CASCADE)
    title = models.CharField(_('title'), blank=True, max_length=50)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    qty = models.IntegerField(_('qty'))
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
