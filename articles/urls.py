from django.urls import path
from .views import articles, articleById

urlpatterns = [
    path('', articles, name='products'),
    path('<int:pk>/', articleById, name='productById')
]