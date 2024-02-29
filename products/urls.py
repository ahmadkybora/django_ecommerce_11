from django.urls import path
from .views import products, productById

urlpatterns = [
    path('', products, name='products'),
    path('<int:pk>/', productById, name='productById')
]