from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='%(class)s', on_delete=models.CASCADE)
    qty = models.IntegerField(_('qty'))
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

